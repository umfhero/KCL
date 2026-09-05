# Running KCL study space

Double-click `START_STUDY.cmd` to open the local dashboard at http://127.0.0.1:4826. It uses your existing Codex sign-in and Luna at medium reasoning effort. It does not require OpenCode or a new API key.

The app opens on the module overview with an empty personal library. Add your own PDFs, Markdown or text files in Source library, select the sources needed for a question, then use Save explanation when you want to keep an answer in Saved notes.

## Local setup

- Code and sources: this repository. Sources are under `sources/2026-27/<module>/` and ignored by Git. This checkout is under OneDrive, which can still synchronise ignored files.
- Database, model workspace, browser profile and logs: `%USERPROFILE%\Desktop\KCL\study-data` by default. Override with the `KCL_STUDY_DATA` environment variable if needed. Never use a synchronised folder for a live SQLite database or browser profile.
- Frontend dependencies may be ordinary repo-local `node_modules`, or an external location supplied through the `KCL_NODE_MODULES` environment variable.
- The server binds only to `127.0.0.1`. No public hosting or friend access has been configured.

For a fresh installation, use Python 3.11 or later, install `requirements.txt`, install the package.json dependencies, run `npm run build`, then run `python -m server.main`. Sign into Codex with `codex login` before starting model requests. The current machine has the required Python packages installed. Frontend versions are pinned in package.json.

To rebuild, run `node scripts/build.mjs`. To start without opening a browser, run `powershell -NoProfile -File scripts/start.ps1 -NoBrowser`. To stop the saved app process, run `powershell -NoProfile -File scripts/stop.ps1`.

## Source collection

Choose a module, enter its stable course-page URL or a direct PDF URL, then choose Collect PDFs. The collector checks up to 35 links and imports up to 20 PDFs per job, with a 50 MB per-file limit. It follows same-site PDF links and Moodle resource/folder links. This first version does not crawl arbitrary websites or export every Moodle activity type.

For KEATS, choose Sign into KEATS to open a dedicated local study browser. Sign in normally, close that browser, select Use my study-browser sign-in, and collect the stable module URL. Expired sessions appear as Sign-in required. Browser login credentials and session state are not copied into Git. DRM-protected or unavailable readings remain manual imports from authorised copies.

Choose Scan local folders after adding documents directly to the module folder. Imported versions are immutable, so earlier citations keep their original PDF. Identical content is deduplicated within a module. Text-only PDFs are indexed; pages with little extracted text are flagged for review. OCR and semantic retrieval are not enabled in this build.

## Model and learning scope

The notebook searches the selected local sources, then sends relevant passages and a short conversation context to Codex. Model tool use, shell execution, connectors and file editing are disabled for study requests. Responses include validated source references, optional concept diagrams and practice questions. Numerical RSA visuals use local deterministic calculations rather than model-generated executable code.

The source library is empty on a fresh installation, and each user must add their own authorised course files. Assessment facts in the course guide date from the existing README and need checking against current KEATS pages. Signed-in KEATS collection still needs testing with your current module pages.

Codex plan limits still apply. Luna is fixed as the default, with no automatic switch to a more expensive model. The app handles one answer at a time and persists successful conversations in SQLite. It does not charge a separate hosting fee.

Use Export notes, chats and progress in Settings for a portable JSON copy, and keep original documents backed up separately. Automated database backups and scheduled collection are follow-up work.
