# KCL MSc Cyber Security — Course Overview

A quick-reference guide for anyone starting the MSc Cyber Security at King's College London in September 2026, covering programme structure, credit breakdown, assessment patterns, key dates, and pre-arrival prep priorities.

---

## Programme at a Glance

| Detail              | Info                                                       |
| :------------------ | :--------------------------------------------------------- |
| **Total Credits**   | 180 (120 taught + 60 project)                              |
| **Duration**        | 1 year full-time                                           |
| **Department**      | Informatics, King's College London                         |
| **Certification**   | NCSC-certified (valid until 30 Sep 2026, renewal expected) |
| **Research Centre** | King's Cybersecurity Centre (EPSRC-NCSC ACE-CSR)           |
| **Campus**          | Bush House / Strand, London                                |

---

## Academic Calendar

| Period            | Dates (approx.)     | What happens                                      |
| :---------------- | :------------------ | :------------------------------------------------ |
| Welcome Week      | w/c 21 Sep 2026     | Induction, enrolment, faculty sessions            |
| Autumn Semester   | Sep – Dec 2026      | Cryptography, Security Engineering, Security Mgmt |
| Winter Break      | Dec 2026 – Jan 2027 |                                                   |
| Spring Semester   | Jan – Apr 2027      | Network Security, Security Testing, Forensics     |
| Project Execution | May – Sep 2027      | Individual Project write-up and submission        |

---

## Credit Structure

```
┌─────────────────────────────────────────────────────────┐
│                   180 CREDITS TOTAL                      │
├─────────────────────────┬───────────────────────────────┤
│   120 TAUGHT CREDITS    │      60 PROJECT CREDITS       │
│                         │                               │
│  6 x Compulsory (90cr)  │    Individual Project         │
│  2 x Optional   (30cr)  │    (dissertation + artefact)  │
└─────────────────────────┴───────────────────────────────┘
```

Each 15-credit module = **8.3%** of the final degree.
The Individual Project = **33.3%** of the final degree.

---

## Compulsory Modules

| Module                            | Code     | Credits | Semester | Assessment          |
| :-------------------------------- | :------- | :-----: | :------: | :------------------ |
| Cryptography                      | 7CCSMCIS |   15    |  Autumn  | 100% Exam           |
| Security Engineering              | 7CCSMSEN |   15    |  Autumn  | 70% Exam / 30% CW   |
| Security Management               | 7CCSMSEM |   15    |  Autumn  | Exam + Essay/Report |
| Security Testing                  | 7CCSMSTE |   15    |  Spring  | Exam + Practical CW |
| Network Security                  | 7CCSMNSE |   15    |  Spring  | ~85% Exam / ~15% CW |
| Computer Forensics and Cybercrime | 7CCSMCFC |   15    |  Spring  | Exam + Coursework   |
| Individual Project                | 7CCSMPRJ |   60    |   Full   | 100% Project        |

---

## Optional Modules (Choose Two)

You pick 30 credits (two modules) from a list of optionals. KCL shares electives across its Informatics MSc programmes, so the available pool is wider than just cybersecurity-specific modules. The exact list for 2026/27 will be confirmed at enrolment, but the following have appeared as options for MSc Cyber Security students in recent years:

| Module                           | Code     | Credits | Semester | Assessment             | Notes                                     |
| :------------------------------- | :------- | :-----: | :------: | :--------------------- | :---------------------------------------- |
| Machine Learning                 | 7CCSMMML |   15    |  Spring  | Exam + Coursework      | Maths-heavy, shares with AI MSc           |
| Distributed Ledgers and Crypto   | 7CCSMDLC |   15    |  Spring  | Coursework + Practical | Blockchain, consensus, smart contracts    |
| Software Measurement and Testing | 7CCSMASE |   15    |  Autumn  | 85% Exam / 15% CW      | White/black-box testing, coverage metrics |
| Big Data Technologies            | 7CCSMBDT |   15    |    —     | Not confirmed          | Data pipelines, MapReduce, analytics      |
| Agents and Multi-Agent Systems   | 7CCSMAMS |   15    |  Autumn  | Not confirmed          | Shared with Advanced Computing MSc        |

> This list is based on publicly available information and may not be exhaustive. Some modules from the wider Informatics catalogue (e.g., Nature-Inspired Learning, AI Planning) may also be selectable subject to timetabling and programme director approval. The definitive list is provided during module selection in September.

---

## Assessment Weight Summary

```
Individual Project   ██████████████████████████████████░  33.3%
Cryptography         █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Security Engineering █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Security Management  █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Security Testing     █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Network Security     █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Forensics            █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Optional A           █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
Optional B           █████████░░░░░░░░░░░░░░░░░░░░░░░░░   8.3%
```

---

## Module Dependencies

Some modules have prerequisites or assumed knowledge that matters for sequencing.

```
Cryptography (Autumn)
    ├── required for ──▶ Network Security (Spring)
    └── required for ──▶ Computer Forensics and Cybercrime (Spring)

Security Engineering (Autumn)
    └── assumed knowledge for ──▶ Security Testing (Spring)
```

---

## Pre-Arrival Prep Priorities

These are the areas worth covering before September, ordered by how directly they feed into specific modules.

| Priority | Area                             | Why it matters                                                | Feeds into                         |
| :------: | :------------------------------- | :------------------------------------------------------------ | :--------------------------------- |
|    1     | Discrete maths and number theory | Modular arithmetic, Euler's theorem, Extended Euclidean Algo  | Cryptography, Network Security     |
|    2     | C/C++ and x86 assembly           | Memory management, pointers, stack layout, basic OS internals | Security Engineering               |
|    3     | TCP/IP and networking            | Protocol stack, packet structure, DNS, HTTP, routing basics   | Network Security, Security Testing |
|    4     | Web application fundamentals     | HTTP methods, cookies/sessions, SQL, web architecture         | Security Testing                   |
|    5     | IT governance and UK cyber law   | GDPR, Computer Misuse Act, incident response frameworks       | Security Management, Forensics     |

---

## Free Resources Worth Starting Now

| Resource                                       | Covers                       | Link                                             |
| :--------------------------------------------- | :--------------------------- | :----------------------------------------------- |
| Anderson, _Security Engineering_ (3rd ed.)     | Security engineering, design | cl.cam.ac.uk/archive/rja14/book.html             |
| PortSwigger Web Security Academy               | Web app security, pentesting | portswigger.net/web-security                     |
| CyBOK (Cyber Security Body of Knowledge)       | Cross-cutting reference      | cybok.org                                        |
| OWASP Web Security Testing Guide v4.2          | Security testing methodology | owasp.org/www-project-web-security-testing-guide |
| NIST Cybersecurity Framework 2.0               | Governance, risk management  | nist.gov/cyberframework                          |
| Narayanan et al., _Bitcoin and Cryptocurrency_ | Distributed ledgers          | bitcoinbook.cs.princeton.edu                     |

---

## Individual Project (33.3% of Degree)

The project runs across the full year, with formal proposal development happening in the Spring semester through the Informatics Project Proposal (IPP) module.

| Stage             | When            | What                                                  |
| :---------------- | :-------------- | :---------------------------------------------------- |
| Topic exploration | Autumn semester | Browse staff research interests, attend project talks |
| IPP module        | Spring semester | Develop formal proposal with allocated supervisor     |
| Project execution | May – Sep 2027  | Build artefact, run experiments, write dissertation   |
| Submission        | September 2027  | Final dissertation + artefact                         |

Topic selection works in three ways: picking from a staff-proposed list, proposing your own topic with a willing supervisor, or working with an external partner through the Knowledge Exchange Projects (KEPs) scheme.

---

## Community and Contacts

| What                              | Where                                             |
| :-------------------------------- | :------------------------------------------------ |
| KCL Cyber Security Society (KCSS) | discord.com/invite/aRQETvq22Z (~430 members)      |
| KCSS Instagram                    | @kclcybersociety                                  |
| KCL Tech Society                  | kclsu.org (runs TechSummit, hackathons)           |
| Welcome to King's app             | Available from mid-August via KCL                 |
| KCL offer holder info             | kcl.ac.uk/study/postgraduate-taught/offer-holders |

---

## Degree Classification Boundaries

| Classification | Threshold |
| :------------- | :-------- |
| Distinction    | 70%+      |
| Merit          | 60–69%    |
| Pass           | 50–59%    |

---

_Last updated: April 2026_
