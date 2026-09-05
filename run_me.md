# Run the KCL study space

This app runs on your own computer, so clone the repository, add your own course files and sign in with your own Codex account. Nothing needs to be hosted, and the repository does not contain anyone else's documents, chats or API credentials.

## What you need

Install Git, Node.js with npm, Python 3.11 or later, and the Codex CLI before continuing. You can confirm they are available in PowerShell with the following commands:

```powershell
git --version
node --version
npm --version
python --version
codex --version
```

## Clone and install

Clone the repository, open PowerShell inside the cloned folder, then install the Python and frontend packages:

```powershell
git clone <repository-url>
cd KCL
python -m pip install -r requirements.txt
npm install
npm run build
```

Replace `<repository-url>` with the Git URL shared for this project. Each person should run these commands in their own clone rather than sharing one installed copy.

## Add and scan your course content

Put each PDF, Markdown or text file into the folder for its module:

```text
sources/
  2026-27/
    7CCSMCIS/    Cryptography files
    7CCSMSEM/    Security Management files
    7CCSMSEN/    Security Engineering files
    6CCSARDM/    Agent Reasoning and Decision Making files
    7CCSMCFC/    Computer Forensics and Cybercrime files
    7CCSMNSE/    Network Security files
    7CCSMSCT/    Security Testing files
    7CCSMBDT/    Big Data Technologies files
    7CCSMPRJ/    Individual Project files
```

The app creates these folders (and `sources/2026-27/PERSONAL/`) on its first run if they do not exist. Because this repository is itself in a shared/synchronised OneDrive checkout, authorised shared course content can be placed directly in `sources/2026-27/<module-code>/`. Put contracts, disability documents and other miscellaneous personal files in `sources/2026-27/PERSONAL/` instead. Then open **Source library** and choose **Scan local folders**. You can also upload files from the Source library page.

The `sources` folder is ignored by Git, so these files will not be committed when you push code. Git ignore does **not** stop OneDrive synchronising them: only place personal contracts or disability documents there when the sharing permissions for this OneDrive location are appropriate. Chats, notes and saved-chat session state persist in the SQLite database at `KCL_STUDY_DATA` between runs.

## Sign in and start

The app does not use a shared application API key, because every user signs into Codex with their own account and uses their own plan allowance. Sign in once with:

```powershell
codex login
```

Later, run these commands from the repository after pulling any code changes:

```powershell
npm install
npm run build
python -m server.main
```

You can also double-click `START_STUDY.cmd`, or start it from PowerShell with:

```powershell
python -m server.main
```

Open <http://127.0.0.1:4826> if the browser does not open automatically.

## Optional local settings

The app normally stores its database and model workspace under `%USERPROFILE%\Desktop\KCL\study-data`, which keeps live SQLite files out of OneDrive. You can choose another non-synchronised folder or port for the current PowerShell session:

```powershell
$env:KCL_STUDY_DATA = "$env:LOCALAPPDATA\KCL-study-data"
$env:KCL_PORT = "4826"
python -m server.main
```

Do not commit `.env` files, API keys, course documents or exported study data. If Codex requests fail, run `codex login` again and use **Settings and storage** in the app to check the connection.
