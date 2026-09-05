# Project context

- KCL Study Space is a local, per-user app. Runtime data defaults outside the repository; it is not a shared hosted workspace.
- User course content belongs under `sources/2026-27/<module-code>`. `sources/` is gitignored, so course files must not be committed.
- Codex access is per user: each installation uses that user's own `codex login`; there is no shared application API key.
- Fresh installs intentionally start with empty sources, chats and tasks. Startup cleanup removes only recognised legacy generated source records; if a user has replaced one of those files, its hash mismatch preserves the replacement.
- UI readability targets 16px body text and 14px metadata, using dark bold text and Lucide icons.
- `run_me.md` is the onboarding guide and documents installation, course-file placement, login and startup.

## Verification

From the repository root:

```powershell
npm run check
npm run build
npm run test:overview
python -m unittest discover -s tests -p "test_*.py"
```
