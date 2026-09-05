# Architecture notes

- The frontend is React/TypeScript in `app/`, built by `scripts/build.mjs`; icons come from `lucide-react`.
- The local Python server lives in `server/` and owns runtime storage, source ingestion, retrieval and startup cleanup.
- Course sources are organised by academic year and module beneath `sources/2026-27/`; chats, tasks and other runtime state are intentionally local to the user.
- Generated source cleanup is identity-aware: recognised generated records are removed only when their stored file still matches the recorded content hash, preserving user replacements.
