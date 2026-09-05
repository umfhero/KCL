# First working build, 5 September 2026

The app runs at http://127.0.0.1:4826 with a React and TypeScript interface, a Python FastAPI backend and a local SQLite database. GPT-5.6 Luna at medium reasoning uses the existing ChatGPT-authenticated Codex App Server. No OpenCode installation or new API key is needed.

## Available to try

- Seven compulsory modules grouped by semester and project, with two selectable electives.
- The existing course guide and summer plan available inside the dashboard.
- Preparation tasks with saved progress weighted by suggested time, separate from the credit-based workload estimate.
- Embedded module chat with selected sources, page citations, bounded conversation context, illustrative concept connections and practice questions.
- An interactive Cryptography lab that calculates a toy RSA example locally.
- PDF, text and Markdown imports, local search, immutable source versions, saved explanations and a JSON export of personal study data.
- Collection of accessible PDF links and Moodle resource/folder links from a supplied page. A dedicated Edge sign-in flow is available for KEATS.

The library is empty on a fresh clone, so each user adds their own authorised lectures, readings and notes under `sources/2026-27/<module-code>/`.

## Verification

Two real Luna requests completed successfully: an explanation with a diagram and quiz from the preparation notes, and an explanation citing pages 20 and 21 of the downloaded mathematical-background chapter. They took approximately 16 and 21 seconds in these checks; response times will vary.

Five isolated backend tests cover module and source selection boundaries, immutable document versions, duplicate imports, rejecting files outside the library, private-address URL rejection and invalid citation references. Live HTTP checks passed for origin and host restrictions, mutation tokens, empty-evidence handling and data export.

Edge browser checks passed for the module overview, citation viewer, practice quiz, RSA controls, progress persistence, course-guide rendering and passage search. Overview widths of 1440, 1024, 768 and 390 pixels had no horizontal overflow, and the mobile RSA view also passed. No page JavaScript errors were reported. The frontend was type-checked and built.

## Remaining work

KEATS collection needs testing against the user's signed-in current module pages. Current lectures, module handbooks and assigned book copies have not been collected. The public textbook collector is verified; authenticated KEATS collection is not yet verified.

Retrieval currently uses SQLite full-text search with page-preserving chunks. Semantic retrieval, OCR, a reviewed syllabus-to-lesson map, more interactive labs, automatic source checks, database backups and friend accounts remain future work. Jobs interrupted by a restart are marked for retry. They do not resume automatically.

The app binds to loopback only. The source folder is ignored by Git but remains inside the existing OneDrive checkout and can still sync through OneDrive. The live database, browser profile and model workspace are under the separate Desktop KCL folder.
