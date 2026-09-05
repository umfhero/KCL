# Summer Revision - 6 Week Plan (1-2 hours/day)

You already have strong networking and crypto math, so this plan focuses on C fundamentals, memory, debugging, and secure coding. Everything should be done in your local Kali VM or lab environment only.

## Daily Structure (60-120 mins)

- 25-40 min video/interactive lesson
- 25-40 min hands-on C exercise
- 10-15 min recap notes (1-2 takeaways, 1 question)

## 6 Week Plan

| Week | Focus                                                      | Video/Interactive                                            | Hands-on (C)                                                         | Done |
| ---- | ---------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------- | ---- |
| 1    | C basics (types, control flow, functions, arrays, strings) | learn-c.org (C basics)                                       | Build a small CLI tool: calculator, unit converter, or text stats    | [ ]  |
| 2    | Pointers, structs, stack vs heap                           | learn-c.org (pointers, structs) + Beej's Guide to C (memory) | Build a dynamic array and a struct-based record list                 | [ ]  |
| 3    | Memory errors and tooling                                  | AddressSanitizer intro (gcc -fsanitize=address)              | Introduce a bug (use-after-free, out-of-bounds), then fix it         | [ ]  |
| 4    | Debugging with gdb                                         | OpenSecurityTraining2 (GDB intro)                            | Debug a crashing program from Week 3 using breakpoints and backtrace | [ ]  |
| 5    | Secure coding basics                                       | SEI CERT C (input validation, bounds checks)                 | Refactor earlier programs to validate input and cap lengths          | [ ]  |
| 6    | C to assembly mapping (light)                              | OpenSecurityTraining2 (x86-64 intro)                         | Compile with -S and map C variables to assembly blocks               | [ ]  |

## Optional (if you want extra)

- Practice on a local CTF-style lab only (Exploit Education - Phoenix) to recognize bug patterns without targeting real systems.
- Keep a running glossary: pointer, stack frame, heap allocation, undefined behavior, bounds check.

## Suggested tools (Kali VM)

- gcc, gdb, make
- AddressSanitizer: gcc -fsanitize=address -g -O0
- Optional: valgrind
