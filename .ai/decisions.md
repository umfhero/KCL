# Decisions

- Keep course material and runtime study data local/per-user rather than adding shared storage or a shared API credential.
- Keep `sources/` gitignored and start a fresh installation with empty sources/chats/tasks to avoid shipping personal state.
- Treat generated-source cleanup as safe deletion only on hash match; a changed file is user-owned and must remain.
- Use 16px body text, 14px metadata, dark bold text and Lucide icons as the current readability baseline.
