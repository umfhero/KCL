"""Isolated checks for source boundaries, immutable citations and retrieval."""
import tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from server import store
from server.model import validate_response
from server.collector import valid_url

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.patch=patch.multiple(store,DATA=self.root/'data',SOURCES=self.root/'sources')
        self.patch.start(); store.init()
    def tearDown(self):
        self.patch.stop(); self.temp.cleanup()
    def document(self,module,name,text):
        p=store.SOURCES/module/name; p.write_text(text,encoding='utf-8')
        return p,store.ingest(p,module)
    def test_module_and_selection_boundaries(self):
        _,sid=self.document('7CCSMCIS','a.txt','Elliptic curve arithmetic uses finite field operations. '*8)
        _,other=self.document('7CCSMNSE','b.txt','Elliptic curve arithmetic is deliberately in a different module. '*8)
        results=store.retrieve('7CCSMCIS','elliptic',[sid,other])
        self.assertTrue(results)
        self.assertEqual({r['source_id'] for r in results},{sid})
        self.assertEqual(store.retrieve('7CCSMCIS','elliptic',[]),[])
        self.assertEqual(store.retrieve('7CCSMCIS','elliptic',[other]),[])
    def test_immutable_version_and_deduplication(self):
        p,first=self.document('7CCSMCIS','version.txt','Original evidence about multiplication and inversion. '*6)
        self.assertEqual(store.ingest(p,'7CCSMCIS'),first)
        p.write_text('Revised evidence about polynomial operations. '*8,encoding='utf-8')
        second=store.ingest(p,'7CCSMCIS')
        self.assertNotEqual(first,second)
        with store.db() as c: row=c.execute('SELECT path FROM sources WHERE id=?',(first,)).fetchone()
        self.assertIn('Original evidence',Path(row['path']).read_text())
    def test_files_outside_library_rejected(self):
        p=self.root/'private.txt'; p.write_text('Private content')
        with self.assertRaises(ValueError): store.ingest(p,'7CCSMCIS')
    def test_legacy_cleanup_preserves_replaced_user_file(self):
        original=store.SOURCES/'7CCSMCIS'/'module-guide.md'
        original.write_text('Old generated module guide content. '*5,encoding='utf-8')
        source_id=store.ingest(original,'7CCSMCIS','Course guide: Cryptography','readme.md','guide')
        with store.db() as c:
            version=Path(c.execute('SELECT path FROM sources WHERE id=?',(source_id,)).fetchone()['path'])
        original.write_text('My replacement module notes must remain. '*5,encoding='utf-8')
        store.clean_generated_sources()
        self.assertTrue(original.exists())
        self.assertFalse(version.exists())
        self.assertEqual(store.list_sources(),[])
    def test_private_web_address_rejected(self):
        with self.assertRaises(ValueError): valid_url('http://127.0.0.1/private.pdf')
        with self.assertRaises(ValueError): valid_url('file:///C:/private.pdf')
    def test_invented_reference_rejected(self):
        with self.assertRaises(ValueError): validate_response({'answer':'Claim [S99]','source_refs':['S99']},[{'ref':'S1'}])
    def test_course_guide_response_can_be_uncited_when_no_indexed_source_is_selected(self):
        response=validate_response({'answer':'The programme guide says to check the current handbook.','source_refs':[],'diagram':{},'quiz':{}},[])
        self.assertFalse(response['grounded'])
        self.assertEqual(response['citations'],[])
    def test_personal_folder_and_global_session_are_available(self):
        self.assertTrue((store.SOURCES/'PERSONAL').is_dir())
        session=store.create_session('global')
        self.assertIsNone(session['module'])
        self.assertEqual(store.sessions('global')[0]['id'],session['id'])
    def test_complete_module_record(self):
        self.assertEqual(len(store.MODULES),9)
        self.assertEqual(sum(module['credits'] for module in store.MODULES),180)
        self.assertEqual({module['id'] for module in store.MODULES if module.get('elective')},{'6CCSARDM','7CCSMBDT'})

if __name__=='__main__': unittest.main()
