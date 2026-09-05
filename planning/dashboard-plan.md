# KCL study dashboard proposal

Revised for local operation, 5 September 2026. The user has chosen a personal app running on their Windows PC, with documents stored in the local project and chat inside the dashboard. This supersedes the hosted Cloudflare proposal. A working first build now uses GPT-5.6 Luna at medium reasoning through the official local Codex App Server, verified with the user's existing ChatGPT sign-in. There is no separate hosting or API-key connection. Codex plan limits apply. Friends sharing remains a later option, with personal use first.

The sections below describe the wider design, including work still to build. See [the current build record](build-status.md) and [running instructions](../RUNNING.md) for the implemented scope. This version has local full-text retrieval and collection started from the dashboard. Embeddings, OCR, automatic scheduled updates and resumable worker processes are future work.

## Recommended direction

Build a custom dashboard and prove its chat quality using Cryptography first. Use a semester overview as the home page, a notebook layout inside each module, and a weekly planner for personal revision. These views can belong to one app, although the mock-up lets us compare which should take priority.

Use React and TypeScript for the browser dashboard, a local Python FastAPI service, and SQLite for course data, source passages, conversations and progress. Local extraction and embeddings prepare the search index. The backend retrieves passages and calls a replaceable model connector: direct API, Codex App Server, OpenCode running locally, or Ollama. There is no dependency on Google's NotebookLM product.

Serve the built dashboard and API from one local origin. Use one launcher and an optional Windows login task to start the app and the selected model service. Heavy imports run in a background worker process, with job state in SQLite. On restart, interrupted jobs resume safely. Close or suspend the PC and background collection stops; the next run checks for missed updates.

Source files and app data stay on the PC. If an external model is selected, the question, selected source excerpts and a bounded conversation history leave the PC for inference. Fully local inference avoids that transfer. An API key does not make inference free, and routing through OpenCode does not change the provider's charges or account limits.

## What is already in the repository

The current checkout is the repository checkout, with its configured Git remote.

- `readme.md` contains the programme structure, registrations, elective options, assessment notes, dates, preparation priorities, resources and KCL links. Its registration snapshot is dated 24 August 2026.
- `KCLBrief.md` contains earlier research, with some claims that differ from the later README. For example, it uses the older Security Testing code and contains assessment estimates. Import it as background research pending review, not as authoritative module data.
- `summer revision.md` contains a six-week preparation plan, and is currently untracked. Preserve it.
- `Cyber Security MSc` contains 14 course-note placeholders, 14 revision guides and a 3.2 MB book PDF. It is not empty. Some revision guides contain useful preparation topics, but their assessment and prerequisite claims need checking.

Before removing the old folder, inventory and hash its files, migrate useful notes, and preserve the book under the new local sources structure. Verify the migrated copies before deleting any original. Correct `7CCSMSTE` to the README's `7CCSMSCT` in the new module catalogue. Local files can live inside the project without being committed. Commit code, reviewed course metadata and personal notes intended for version control; keep downloaded restricted material, generated indexes, credentials and private chat state out of commits by default. Check the existing book's Git history and repository visibility before later public sharing.

The current checkout is under OneDrive. A gitignore rule does not disable OneDrive synchronisation, and keeping a file available offline does not prevent its upload. For genuinely local operation, use a verified unsynchronised checkout containing both code and app data. If the user retains the OneDrive checkout for code, place mutable runtime data in a separate unsynchronised local directory. Do not move the checkout or alter sync settings during planning.

Only selected module folders should feed the importer. It must not recursively ingest the wider Coursework or Desktop KCL folders.

## Course map

KCL's public course page currently confirms the six compulsory taught modules and the 60-credit project. Semester placement and codes below come from the local README, and still need checking against the current authenticated module record before launch. [KCL course page](https://www.kcl.ac.uk/study/postgraduate-taught/courses/cyber-security-msc/teaching)

| Period | Module | Code | Credits |
| :-- | :-- | :-- | --: |
| Semester 1 | Cryptography | 7CCSMCIS | 15 |
| Semester 1 | Security Management | 7CCSMSEM | 15 |
| Semester 1 | Security Engineering | 7CCSMSEN | 15 |
| Semester 1 | Personal elective slot | To be selected | 15 |
| Semester 2 | Computer Forensics and Cybercrime | 7CCSMCFC | 15 |
| Semester 2 | Network Security | 7CCSMNSE | 15 |
| Semester 2 | Security Testing | 7CCSMSCT | 15 |
| Semester 2 | Personal elective slot | To be selected | 15 |
| Project | MSc Individual Project | 7CCSMPRJ | 60 |

Each friend selects their own electives. The shared compulsory modules remain the same, while their planner and overall workload use their own selections. The README records 150 registered credits and two remaining choices; this is a dated personal snapshot, not the registration state of every visitor.

## Page structure and design concepts

### A. Semester overview

A clean white page with a narrow navigation column, restrained blue accents, readable type and compact module cards. Each semester groups its compulsory modules and elective slot, with the project below. A preparation section remains available before teaching starts.

Each module shows its next study task, completed work, estimated remaining hours, source freshness and an Open notebook action. Missing schedules say Awaiting module schedule. The home page should not imply that suggested reading is already indexed or that the module has been completed because its teaching period has ended.

This is the strongest home page because it keeps the whole degree visible.

### B. Module notebook

A source list on the left, a central conversation, and a compact revision area. Users can include or exclude readings, ask questions with citations, open the cited passage, save an answer privately, or turn it into practice questions. On mobile, Sources, Chat and Revision become separate views.

The module page also contains its overview, weekly topics, reading list and assessments. Put the official reading list first, and label preparation resources separately. The chat can explain, compare, give a worked example, test recall, or provide hints before revealing an answer.

This is the main study view, with the semester overview one click away.

### C. Weekly study plan

A short list of study sessions grouped by day, with estimated time and module links. Users set weekly availability, and unfinished tasks can be rescheduled. Preparation, term-time study and exam revision use the same planner.

This is useful for regular study, but works better as a second page because it gives less context about the whole degree.

### Reorganising the README

| Existing information | Dashboard destination |
| :-- | :-- |
| Programme summary and credit structure | Course guide |
| Current registrations and electives | My modules, with a per-user selection state |
| Module topics, assessments and reading | Individual module pages |
| Academic calendar | Dates and planner |
| Preparation priorities and summer plan | Preparation |
| Useful KCL links | Course guide and contextual module links |
| Classification and condonement notes | Course guide, with current handbook links |
| Source and update notes | Visible source date and status on relevant records |

Retain a short repository README explaining the app, setup and content provenance. Use structured course data to generate the dashboard and any course-guide export, so the two do not drift. Do not infer exam dates from general assessment periods.

## Local technology stack

| Part | Proposed implementation | Purpose |
| :-- | :-- | :-- |
| Dashboard | React, TypeScript and Vite | The agreed clean UI, module notebooks and progress views |
| Local backend | Python and FastAPI | Serve the built dashboard, source search, chat streaming and file access |
| Database | SQLite with FTS5 | Local metadata, full-text passages, chats, tasks and progress |
| Semantic retrieval | Locally generated embeddings, stored as versioned local arrays | Find relevant material even when a question uses different wording |
| Document processing | pypdf for text PDFs, optional local OCR, format-specific parsers | Preserve page, heading and slide references |
| PDF reader | PDF.js in the dashboard | Open the original local PDF at the cited page |
| Source collection | Supported Moodle API where available; otherwise a dedicated signed-in browser collector | Download accessible module resources in a repeatable way |
| Model connector | OpenAI API, Codex App Server or OpenCode adapter | Keep model access replaceable without changing course data or the UI |
| Local alternative | Ollama | Optional local embedding and answer generation |
| Visuals | Mermaid, KaTeX and validated interactive React components | Diagrams, equations, worked examples and small simulations |

SQLite remains the record of truth. For the first module, load only its embedding matrix and compute similarity locally, then combine those results with full-text ranking. At 20,000 passages and 384 float32 dimensions, the raw vectors occupy about 30.7 MB, excluding metadata and runtime overhead. This is a sizing example; benchmark the chosen model and corpus before selecting a larger vector engine. Do not add a separate database server until measurements justify it.

Ollama exposes an embedding endpoint, but the embedding model is a separate choice from the chat model. Select and version one embedding model, and rebuild affected indexes when it changes. [Ollama embedding API](https://docs.ollama.com/api/embed).

Use locked dependencies and one local service launcher. Bind to loopback, enforce allowed origins and protect administrative actions. Run imports outside the web request process, queue them in SQLite, and publish a new index only after validation. The UI shows whether the backend, index and model are ready, and offers retry or cancellation for imports.

## How the notebook chat works

The notebook is a view over local records: a module, its sources, a topic map, conversations, generated revision material and progress. It is not a Google notebook and does not require uploading the library to NotebookLM.

```text
Question in the module dashboard
  -> local retrieval of relevant pages and prerequisite topics
  -> bounded evidence packet, learning context and answer instructions
  -> chosen model through API, Codex or OpenCode
  -> validated explanation, citation references and visual specification
  -> answer and interactive visual rendered in the dashboard
```

The app saves local conversation history and selects the useful part for each request. It does not resend every textbook or every prior message. Clicking a citation opens the version of the source used for that answer at its actual page, with physical PDF page and printed page label distinguished.

### Model access and cost

The user has existing Codex access and prefers a lower-cost model such as Luna, with GPT-5.5 as another candidate. Start by establishing the account's actual authentication mode and available models without copying credentials out of their store.

- If the access is an OpenAI Platform API key, a direct Responses API connector is the simplest route. Keys stay in backend credential storage.
- If it is ChatGPT-backed Codex access, investigate the official local Codex App Server. It supports custom clients and managed ChatGPT authentication. Confirm a successful request and available model list before committing to this route; plan allowances still apply.
- If OpenCode is already the preferred provider interface, use its local server through a backend adapter. It is an alternative connector, not another compulsory layer on top of Codex.

The official documentation distinguishes API-key billing from included ChatGPT access. App Server has managed login and account-limit interfaces, so the dashboard need not scrape or repackage login tokens. [Codex authentication](https://learn.chatgpt.com/docs/auth), [Codex App Server](https://learn.chatgpt.com/docs/app-server).

Current published standard API text prices, checked 5 September 2026:

| Model | Input per million tokens | Output per million tokens | Proposed role |
| :-- | --: | --: | :-- |
| gpt-5.6-luna | $0.20 | $1.20 | First candidate for ordinary teaching, grounded answers and visual specifications |
| gpt-5.5 | $5.00 | $30.00 | Optional review of difficult explanations, only if enabled |

[Luna model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-luna), [GPT-5.5 model documentation](https://developers.openai.com/api/docs/models/gpt-5.5).

For an illustrative 8,000 input tokens and 2,000 billed output tokens, Luna costs $0.004 and GPT-5.5 costs $0.10. One thousand such calls would cost $4 versus $100. These figures exclude additional reasoning output beyond that allowance, retries, images, tools and taxes; they are not a monthly usage forecast. Subscription usage has a different allowance model.

Use Luna provisionally, subject to the teaching-quality pilot. Cache reviewed explanations and visuals by source version, keep retrieval and calculations local, and limit additional model calls. Record actual token use and configure a user-selected budget before billable use. Escalation to GPT-5.5 should be deliberate, with a visible cost implication. Better structure reduces wasted context and errors; it does not guarantee that a smaller model will explain everything correctly.

### Where OpenCode fits

OpenCode documents a headless HTTP server, session APIs, a JS/TS SDK and configurable providers. Our Python backend can call its HTTP interface, while the dashboard remains our own React app. Pin a tested OpenCode version because configuration and API details differ between releases. [OpenCode server](https://opencode.ai/docs/server/), [SDK](https://opencode.ai/docs/sdk/), [providers](https://opencode.ai/docs/providers/).

Use a dedicated study configuration and a separate conversation per module chat. Pass retrieved passages to it, or later expose narrowly scoped read-only tools such as search_module, read_source_page and get_topic_context. The backend must enforce module scope; a prompt is not an access boundary. Disable arbitrary shell, editing, external-directory reads and automatic public sharing for study conversations. Keep the server on loopback with authentication, and route UI requests through the app backend. [Permissions](https://opencode.ai/docs/permissions/), [custom tools](https://opencode.ai/docs/custom-tools/), [sharing](https://opencode.ai/docs/share/).

A separate coding workspace can still use normal OpenCode capabilities for building the application. A model should not need write access to the course library to answer a revision question.

During this planning run, OpenCode and Ollama executables were found. OpenCode's version command failed while accessing its config location, and Ollama could not start because log writes were denied in this environment. This does not establish that either installation is broken for the user, and neither runtime has been verified working for this app.

## Visual teaching and connecting the module

The aim is a guided study system that can explain how topics fit together. Source retrieval answers an individual question; a curriculum layer supplies the wider sequence.

1. Extract official learning outcomes, the weekly schedule and reading assignments into a draft module map. Mark absent information explicitly. Supplementary preparation topics stay labelled as suggestions.
2. Build a topic record with prerequisites, related topics, source references, examples, common misconceptions and practice tasks. Review the map before treating inferred prerequisite links as official requirements.
3. Offer a study path from prerequisites through each taught topic, with a short explanation, a useful visual, a worked example and a check of understanding. Allow the learner to ask questions or jump ahead at any point.
4. Use practice attempts to identify specific gaps, then suggest the relevant earlier topic. Maintain explicit reviewed progress; do not infer understanding from chat length or pages opened.
5. End a section with a synthesis activity connecting its ideas to earlier sections. At module level, provide a revisitable concept map and mixed-topic practice.

Example preparation path: modular arithmetic -> multiplicative inverses -> RSA toy example -> how public-key cryptography appears in protocols. The dashboard can animate the toy calculation, show where each value comes from, and open supporting pages. Cross-module links to Network Security are labelled as conceptual connections and must not suggest that a toy RSA example reproduces modern TLS.

Visual types should match the explanation:

- Sequence diagrams for protocol exchanges and message ordering.
- Labelled memory diagrams for pointers, stack frames and buffer boundaries.
- Threat-model and attack-tree diagrams for Security Engineering.
- Process diagrams and evidence timelines for Forensics.
- Editable tables and sliders for small, deterministic cryptography examples.
- Concept maps showing prerequisites, applications and links between module topics.

The model returns a structured lesson response with source IDs, explanation blocks, a visual specification and practice items. For example, a sequence visual contains participants and ordered messages; a calculator selects an existing trusted template with validated numeric parameters. The app validates these records and renders approved components. The model does not supply unrestricted JavaScript to execute on the PC. Mermaid runs with strict settings, and user-facing links and source IDs are resolved by the backend.

Use local code for arithmetic and state transitions. Validate the conceptual content of diagrams against sources as well as checking their syntax. Add captions and keyboard-accessible alternatives, and distinguish sourced diagrams from illustrative ones. Save useful visuals as local SVG or PNG and their editable specification. Ordinary diagrams need no paid image-generation call. Scanned figures may need local OCR or, with the user's chosen remote model, selected-page image input.

The pilot must evaluate teaching as well as retrieval: can the learner explain the connection after the lesson, does a diagram contradict the text, and does feedback address the actual mistake? A stronger model reviewing every reply would defeat the cost goal; use deterministic checks, a reviewed evaluation set and selective escalation.

## Automatic source collection and organisation

Register each current module page, academic year, handbook link and reading-list page in a local source manifest. Collection targets those pages and approved linked resources, rather than searching the entire university site.

Use Moodle's supported API when KCL exposes it to the account. Moodle documents core_course_get_contents for module content and web-service file URLs, but whether the KCL account can use it is still unverified. [Moodle API functions](https://docs.moodle.org/dev/Web_service_API_functions).

If API access is unavailable, use a dedicated local browser profile. The user signs in normally, including MFA, and the collector follows accessible links within the configured course. Store browser session state privately outside Git and cloud sync. Session expiry changes the job state to Sign-in required and resumes after login; it is not an excuse to bypass access controls.

The collection job should:

1. Enumerate module sections, folders, file resources, handbook links and reading-list links. Retain the module and section hierarchy in metadata.
2. Classify material into handbook, lectures, labs, assessment briefs, readings and books. Match reading-list books by title, author, edition and ISBN when available.
3. Download accessible files to temporary names, validate that the response is the expected file type rather than a login page, then save atomically using a stable resource ID and readable title.
4. Store origin URL, module code, academic year, source ID, hash, last-modified information, retrieval time, resource type and access status. Keep any token-bearing URL out of committed manifests and logs.
5. Detect duplicate content by hash and changed content by resource identity plus hash. Keep previous versions for citations, and retain local copies when a remote link disappears until the user decides to remove them.
6. Extract text with page and section anchors. Route scans to local OCR, and flag low-confidence extraction, damaged equations and missing figures. Import Markdown and text first alongside PDFs, then add slides and other formats as needed.
7. Chunk by section with controlled overlap, generate embeddings locally, and publish a complete new source version to the index. Retry transient failures with backoff and keep the last usable version during failures.
8. Show Discovered, Downloaded, Indexed, Updated, Sign-in required, Unavailable or Needs review. A book title alone is never shown as indexed content.

Check on app start and with a Sync now action. Optionally run a daily scheduled check while the PC is awake, plus a debounced watcher for manually added PDFs. Use conservative concurrency and conditional requests where supported. Never automatically submit coursework, change enrolment or interact with assessment attempts.

For handbooks that are already PDFs, download the originals. For a handbook represented by a Moodle Book or HTML page, use an available complete export or save a versioned snapshot covering all chapters; mark print-to-PDF copies as generated and preserve section anchors.

For core books, prefer full texts offered by the author, publisher or an authorised library download. Reading-list access does not guarantee an unrestricted PDF download. Record unavailable or restricted titles with their legitimate access link and allow the user to add an authorised local copy. Do not bypass DRM or assume that personal access permits later redistribution to friends.

Start with one authenticated module and verify the discovered file list against what the user can see. That check determines how much collection can be unattended, rather than assuming that every module uses identical resource types.

## RAG behaviour and quality

Each request is restricted to the active local profile, module, selected source set and permitted document versions before retrieval. If remote sharing is added, enforce authentication and group access before retrieval. Retrieve relevant passages, pass a bounded context to the model, and return citations pointing to the actual retrieved passages. Never accept a client-supplied module ID as proof of permission.

Current official module material should take priority over older preparation notes. If sources disagree, show the disagreement and dates. If no passage supports an answer, say that the selected sources do not contain enough information. Offer a clearly labelled general explanation only when the user chooses it.

Treat text inside books and course documents as evidence, never as instructions to the app. Citation IDs must resolve to retrieved source records, although that alone does not prove that the cited passage supports the claim. Test support directly using a small reviewed question set.

Combine lexical search for exact technical terms with local semantic retrieval for paraphrases, using rank fusion and module filtering. Use the topic map to include a relevant prerequisite or neighbouring section without pulling in unrelated chapters. Keep the retrieval interface replaceable as the corpus grows.

Pilot acceptance uses approximately 30 questions drawn from approved Cryptography material: direct facts, explanations, calculations, comparisons, absent information, conflicting versions and attempts to access another module or user's material. All citations must resolve correctly, and there must be no access leaks. Review answer correctness and source support manually; aim for at least 90% supported answers on the agreed set before inviting the full group. This is a pilot gate, not a general accuracy guarantee.

## Progress that means something

Keep planned workload, completed work and demonstrated understanding distinct.

- Work completed: total estimated minutes of completed tasks divided by total estimated minutes in the current task plan. A lab should carry more weight than opening a short page.
- Time spent: optional logged study time compared with a planning estimate. Include teaching, reading, practical work and assessment preparation without double-counting scheduled sessions.
- Understanding: topics practised, recent quiz results and topics marked for another attempt. No understanding score until there is evidence.
- Calendar position: where the user is in the module's teaching and assessment schedule. Passing time does not complete tasks.

KCL's credit framework uses 10 notional learning hours per credit, giving a planning baseline of 150 hours for a 15-credit module and 600 for the project. Confirm the current module workload before replacing that baseline with a weekly allocation. These hours include contact time and independent work, and are not an additional revision target. [KCL quality assurance handbook](https://www.kcl.ac.uk/assets/policyzone/governancelegal/qa-handbook.pdf).

For example, completing two 30-minute tasks and a two-hour lab is three completed hours. In a ten-hour preparation plan that is 30% of planned work, regardless of how many files have been opened. Estimate remaining weekly effort from unfinished work and actual weeks remaining, and flag over-capacity plans instead of silently filling every evening.

Use project milestones such as proposal, literature work, experiment, evaluation and writing, with editable weights. Do not apply a lecture checklist to the dissertation. Degree-level study progress may use credit weights, but it must never be labelled earned credits or predicted degree classification.

## Personal storage and later sharing

The first version is a personal local app. Course content, extracted passages, embeddings, chats, progress and saved visuals remain on the PC. Credentials remain in local credential storage and are never committed. A remote inference connector sends selected context to its provider, so local storage does not mean fully offline processing.

Core records: modules, sources, source versions, passages, topic nodes, prerequisite links, lessons, tasks, progress events, practice attempts, chats, messages, citations, saved visuals and ingestion runs. Include a local profile ID now so later multi-user support does not require rewriting every table.

Keep source files inside the local project tree. Git tracks code and reviewed content, while runtime data and restricted downloads remain ignored unless their inclusion is deliberately agreed. Maintain database-consistent backups using SQLite's backup mechanism, plus the originals; do not copy a live database file as the sole backup. The derived search index should be rebuildable from source files and metadata.

Friends can later run their own copy with their own source access and model credentials, or access a properly authenticated instance hosted on this PC through a private connection. The latter requires the PC to be awake and adds user isolation and source-sharing work. Do not expose raw OpenCode or Codex execution, and do not distribute personal provider credentials with the repo. No remote access is part of the initial build.

## Proposed repository layout

```text
readme.md
app/                             React dashboard and trusted visual components
server/                          local API, retrieval and model connectors
content/
  programme.json                 reviewed programme facts with provenance
  modules/                       module metadata and approved source manifests
  guide/                         course guide and preparation material
sources/                         locally stored documents
  2026-27/
    7CCSMCIS/
      handbook/
      lectures/
      labs/
      readings/
      books/
    7CCSMSEM/
    ...
.local/                          ignored local runtime data
  study.sqlite
  indexes/
  extracted/
  visuals/
  logs/
scripts/                         collector, ingestion worker, launcher, backups
migrations/                      SQLite schema
planning/
```

This layout assumes an unsynchronised local checkout. If code stays under OneDrive, relocate `.local` and browser-session state through explicit settings. Runtime-generated files should not automatically become Git changes, and an ignored PDF can still be indexed by the app. Keep the existing folder until the migration inventory and copied-file hashes agree.

## Delivery sequence

| Stage | Output | Completion check |
| :-- | :-- | :-- |
| 1. Verify local access | Confirm model authentication route, local storage location and one module page | One model request and an accurate list of accessible module resources |
| 2. Build local dashboard | Course guide, compulsory modules, elective slots, PDF reader and preparation view | One launcher; files open locally; mobile-width and keyboard checks |
| 3. Build collection and indexing | Organised downloads, incremental updates and local retrieval | A new PDF becomes searchable; duplicates are avoided; expired login is visible |
| 4. Prove the teaching notebook | Luna candidate, page citations, a topic path, worked examples and visuals | Reviewed answer set, correct source anchors, correct calculations and usable diagrams |
| 5. Add personal learning state | Saved notes, practice history, weighted progress and next-topic suggestions | State survives restart and the suggested next step responds to a real knowledge gap |
| 6. Extend across the year | Remaining modules, source refresh and reliable backups | Source-version changes are handled; index can be rebuilt; restore works |

Planning estimate: approximately 3 to 5 focused working days for a useful one-module prototype, and 1 to 3 weeks for reliable collection and a broader teaching system. These are estimates, not delivery commitments; authenticated site behaviour and PDF quality can change the scope substantially.

The pilot uses roughly 30 reviewed questions plus several visual lessons. Include straightforward retrieval, cross-topic synthesis, an absent answer, source conflicts, a misleading document instruction and incorrect student reasoning. Validate groundedness and learning usefulness, measure latency and cost, and only then extend to every module. Files being downloaded successfully is not enough to establish that they were parsed or taught correctly.

## Decisions to make next

Confirmed: personal local operation, embedded chat, organised automatic document collection, a lower-cost model, and visual explanations that connect the module from beginning to end. The preferred design still combines the semester overview, module notebook and personal planner.

The remaining implementation checks are the exact Codex/API authentication route, a verified unsynchronised data location, and one accessible module page for the collector pilot. Luna is the provisional model, while GPT-5.5 is an optional escalation rather than the default. No model calls, bulk downloads, folder migration or runtime configuration changes have been made by this planning update.
