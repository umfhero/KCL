# KCL MSc Cyber Security: Intelligence Brief

Pre-arrival research for September 2026 entry. This document covers every publicly available detail about the programme, from module-level assessment breakdowns to supervisor mapping, NCSC certification, reading lists, project planning, community channels, and the Royal Holloway scholarship parallel track.

The programme is NCSC-certified (valid until 30 September 2026, with renewal expected), delivered by the Department of Informatics at King's, and sits within the Cybersecurity (CYS) research group under King's Cybersecurity Centre, which is an EPSRC-NCSC Academic Centre of Excellence in Cyber Security Research.

---

## 1. Programme Structure

The MSc comprises 180 credits total, split between 120 taught credits and a 60-credit Individual Project. The taught credits break down as six compulsory 15-credit modules (90 credits) plus two optional 15-credit modules (30 credits), and the project runs across both semesters and summer.

| Period            | Dates (approx.) | Activity                                                |
| :---------------- | :-------------- | :------------------------------------------------------ |
| Welcome Week      | w/c 21 Sep 2026 | Induction, enrolment, faculty sessions                  |
| Autumn Semester   | Sep – Dec 2026  | Cryptography, Security Engineering, Security Management |
| Spring Semester   | Jan – Apr 2027  | Network Security, Security Testing, Forensics           |
| Project Execution | May – Sep 2027  | Individual Project write-up and submission              |

Each 15-credit module accounts for approximately 8.3% of the final degree, while the Individual Project alone accounts for 33.3%, which makes it the single most consequential component by a wide margin.

---

## 2. Compulsory Modules

### 2.1 Cryptography (7CCSMCIS, 15 credits, Autumn)

**Assessment:** 100% examination.

This module provides the mathematical backbone of the entire programme and serves as a formal prerequisite for both Network Security and Computer Forensics in the Spring semester. The content covers number theory foundations including modular arithmetic, Euler's theorem, the Extended Euclidean Algorithm, and the Chinese Remainder Theorem, then moves into classical and modern symmetric ciphers (DES, AES), public-key cryptosystems (RSA, ElGamal), key-establishment protocols (Diffie-Hellman, Needham-Schroeder, Kerberos), digital signatures (RSA, ElGamal, DSA), and zero-knowledge protocols (Fiat-Shamir).

This is the module where students with weak discrete mathematics backgrounds struggle most, because the exam is entirely written and requires fluency with mathematical proofs and number-theoretic reasoning under time pressure. Student feedback from the online variant mentions the compressed format feeling rushed for such dense material, though the on-campus version has more contact hours.

**Prior knowledge needed:** Discrete mathematics, modular arithmetic, basic probability. If any of this feels unfamiliar, Katz & Lindell's _Introduction to Modern Cryptography_ (3rd ed., 2025) is the standard text, and working through the number theory chapters before September will save significant time.

### 2.2 Security Engineering (7CCSMSEN, 15 credits, Autumn)

**Assessment:** 70% examination, 30% coursework.

This is the most technically hands-on module in the Autumn semester, covering command injection, x86 assembly, stack-based buffer overflows, shellcode writing, format string vulnerabilities, memory corruption mitigations, secure software development (threat modelling, defence-in-depth), static analysis, and symbolic execution. The coursework component likely involves practical exploit development or secure code analysis.

Students without prior exposure to C/C++ and low-level systems programming will find this module very difficult, because the exploitation content assumes comfort with memory layout, pointers, and basic OS internals. The module code (7CCSMSEN) also appears in the MSc Advanced Software Engineering as a compulsory module, which suggests the content is shared across programmes and taught by the same staff.

**Prior knowledge needed:** C/C++ programming, basic x86 assembly, memory management concepts, familiarity with Linux command-line environments. Ross Anderson's _Security Engineering_ (3rd ed., free online) covers the design philosophy side, while the practical exploitation content requires hands-on lab work that is best prepared for by working through basic buffer overflow exercises.

### 2.3 Security Management (7CCSMSEM, 15 credits, Autumn)

**Assessment:** Not publicly confirmed in detail, but likely includes both examination and coursework (essays/reports) based on programme-level assessment descriptions.

This is the least technical of the compulsory modules, covering risk assessment and management, security auditing, business continuity planning, cost-effective cybersecurity strategy, risk communication, regulatory frameworks, and security governance. The assessment style is likely to include essay-based components, which can catch students from purely technical backgrounds off guard since the writing expectations are different from lab reports or code submissions.

**Prior knowledge needed:** Basic familiarity with organisational IT structures and governance frameworks. Reading through the NIST Cybersecurity Framework 2.0 and SP 800-37 (Risk Management Framework) before September would provide useful context, and both are freely available from nist.gov.

### 2.4 Security Testing (7CCSMSTE, 15 credits, Spring)

**Assessment:** Not publicly confirmed, likely a mix of examination and practical coursework.

This module covers penetration testing methodology, ethical hacking, social engineering, web application attacks, database attacks, system-level attacks, vulnerability assessment, and security testing frameworks. Students learn to implement and report on penetration tests, interpret vulnerabilities, and apply mitigation strategies. This is the module most directly relevant to offensive security careers, and the KCL virtual lab environment supports hands-on practical work.

**Prior knowledge needed:** Networking fundamentals (TCP/IP, DNS, HTTP), web application basics (how HTTP requests work, session management, basic SQL), and ideally some prior exposure to tools like Burp Suite or OWASP ZAP. PortSwigger's free Web Security Academy is the single best preparation resource for this module.

### 2.5 Network Security (7CCSMNSE, 15 credits, Spring)

**Assessment:** Approximately 85% examination, 15% coursework (based on the shared undergraduate module structure).

This module requires completion of Cryptography as a prerequisite. It covers network fundamentals, security of Internet protocols (both wired and wireless), network attacks and countermeasures, and network security protocol evaluation. Student commentary describes the scope as broader than just TCP/UDP, encompassing wireless security, protocol-level attacks, and defence strategies.

**Prior knowledge needed:** Solid understanding of TCP/IP, the OSI model, routing, DNS, and HTTP. The cryptographic foundations from the Autumn module feed directly into understanding how network protocols are secured (and broken), so the two modules are tightly coupled. Stallings' _Cryptography and Network Security_ (7th ed.) is the standard reference.

### 2.6 Computer Forensics and Cybercrime (7CCSMCFC, 15 credits, Spring)

**Assessment:** Not publicly confirmed, likely examination plus coursework.

This module requires Cryptography as a prerequisite. It covers the legal aspects of cybersecurity (UK Computer Misuse Act, GDPR, international legislation), forensic techniques and methodologies, incident management, digital evidence handling, and the cybercrime landscape. Forum commentary describes this module as covering "investigation and cyber crimes" with real-world scenario application.

**Prior knowledge needed:** Cryptography fundamentals (from the Autumn module), basic legal awareness around UK cyber law. Carrier's _File System Forensic Analysis_ is the standard forensics text, though it covers more depth than a single module requires.

### 2.7 Individual Project (7CCSMPRJ, 60 credits, Full Year)

**Assessment:** 100% project (dissertation plus artefact).

This accounts for one-third of the entire degree classification. Covered in full detail in Section 6 below.

---

## 3. Optional Modules (Choose Two, 30 credits)

KCL shares elective modules across its Informatics MSc programmes (Cyber Security, Advanced Computing, Advanced Software Engineering, Data Science), which means the available pool is wider than just cybersecurity-specific modules. The exact list for 2026/27 will be confirmed at enrolment, but the following have appeared as options for MSc Cyber Security students in recent years.

### 3.1 Machine Learning (7CCSMMML, 15 credits, Spring)

**Assessment:** Examination plus coursework.

This is a mathematically demanding module shared with the AI MSc programme. It covers supervised and unsupervised learning, neural networks, kernel methods, ensemble methods, and evaluation metrics. The maths prerequisite is real, as students need comfort with linear algebra, calculus, and probability at a level beyond what most undergraduate CS programmes require.

**Who this suits:** Students who want to work at the intersection of ML and security (e.g., ML-based threat detection, adversarial ML). It is heavy going and the workload is significant.

### 3.2 Distributed Ledgers and Crypto-Currencies (7CCSMDLC, 15 credits, Spring)

**Assessment:** Not publicly confirmed, likely includes practical coursework elements.

This module covers applied cryptography for blockchain, peer-to-peer consensus networks, Bitcoin architecture, Ethereum and smart contracts, mechanism design and game theory, permissioned vs permissionless networks, and the CAP theorem. Lecture material is developed by KCL instructors and hosted at blockchain.kcl.ac.uk. One student commenter noted that mastering this content "gives you a world that needs you," though others have observed it feels peripherally related to core cybersecurity. Strong cryptography knowledge from the Autumn module is a de facto prerequisite.

**Who this suits:** Students interested in blockchain security, smart contract auditing, or fintech security roles.

### 3.3 Software Measurement and Testing (7CCSMASE, 15 credits, Autumn)

**Assessment:** 85% examination, 15% coursework.

This module covers the software lifecycle testing process, including white-box and black-box testing, finite models (control flow graphs, data-flow graphs, finite state machines), coverage metrics, symbolic execution, static analysis, test oracles, and automated test data generation. This is analytically rigorous and focused on software quality assurance methodology rather than security testing specifically, though the two areas overlap in practice. The module shares teaching methods with the Software Systems group and also appears as a compulsory module on the Advanced Software Engineering MSc.

**Who this suits:** Students interested in formal approaches to testing, automated analysis, or research directions involving verification and automated testing tools.

### 3.4 Big Data Technologies (7CCSMBDT, 15 credits)

**Assessment:** Not publicly confirmed.

This module covers managing, organising, mining, analysing, and visualising large data streams. It appears as an option on the online Advanced Cyber Security MSc and on other Informatics MSc programmes. The practical focus is on identifying challenges within big data and applying technologies to overcome them.

**Who this suits:** Students interested in SIEM/SOC work, security analytics, or threat intelligence at scale where processing large volumes of log and network data is core to the job.

### 3.5 Agents and Multi-Agent Systems (7CCSMAMS, 15 credits, Autumn)

**Assessment:** Not publicly confirmed.

This module covers autonomous agent architectures, multi-agent interaction, game theory, negotiation, and cooperation/competition in distributed systems. It appears as an optional on the Advanced Software Engineering and Advanced Computing MSc programmes and has been selected by MSc students alongside cybersecurity modules.

**Who this suits:** Students interested in autonomous security systems, agent-based modelling of adversarial behaviour, or AI-driven security agents. The overlap with offensive security research involving autonomous pentesting agents is worth noting.

### 3.6 Other Potential Options

KCL's Department of Informatics lists additional modules that may be selectable subject to timetabling and programme director approval, including Nature-Inspired Learning Algorithms, AI Planning, and potentially others from the wider level-7 catalogue. The definitive list is provided during module selection in September, and it is worth asking the programme director or current students which options were actually available in previous years.

### Optional Module Summary

| Module                           | Code     | Credits | Semester | Assessment        |
| :------------------------------- | :------- | :-----: | :------: | :---------------- |
| Machine Learning                 | 7CCSMMML |   15    |  Spring  | Exam + Coursework |
| Distributed Ledgers and Crypto   | 7CCSMDLC |   15    |  Spring  | Not confirmed     |
| Software Measurement and Testing | 7CCSMASE |   15    |  Autumn  | 85% Exam / 15% CW |
| Big Data Technologies            | 7CCSMBDT |   15    |    —     | Not confirmed     |
| Agents and Multi-Agent Systems   | 7CCSMAMS |   15    |  Autumn  | Not confirmed     |

---

## 4. Module Dependencies and Sequencing

Some modules have formal prerequisites or strong assumed-knowledge dependencies that affect how the year flows.

```
Cryptography (Autumn)
    ├── required for ──▶ Network Security (Spring)
    └── required for ──▶ Computer Forensics and Cybercrime (Spring)

Security Engineering (Autumn)
    └── assumed knowledge for ──▶ Security Testing (Spring)

Cryptography (Autumn)
    └── de facto prerequisite for ──▶ Distributed Ledgers (Spring, if selected)
```

The Autumn semester is front-loaded with the hardest foundational material, as Cryptography and Security Engineering run simultaneously and both demand significant preparation time. The Spring semester then builds on those foundations with more applied modules.

---

## 5. Department of Informatics: Staff and Research Mapping

### 5.1 Research Groups and Centres

The department houses three overlapping cybersecurity entities that are relevant to supervision and project alignment.

The **Cybersecurity (CYS) Group** is the core research group, led by Prof Luca Viganò (Head) and Dr Ruba Abu-Salma (Deputy Head). Research themes span AI/ML for cybersecurity, verification and testing, and human factors.

The **Security Hub** is a cross-cutting coordination mechanism within Informatics, co-championed by Prof Jose Such and Dr Abu-Salma, with five explicit themes: AI Cyber Security, Formal Cyber Security, Strategic Cyber Security, Human-Centred Cyber Security, and interdisciplinary connections. The AI Cyber Security theme is defined as covering "both the use of AI for cyber security (including data-driven techniques such as Machine Learning, but also knowledge-based techniques such as Argumentation, Normative Systems, Trust), and the cyber security of AI itself."

The **King's Cybersecurity Centre** is the university-wide EPSRC-NCSC ACE-CSR entity directed by Prof Jose Such, spanning Informatics, War Studies, Defence Studies, Digital Humanities, and the Policy Institute.

### 5.2 Supervisor Shortlist for AI-Assisted Penetration Testing

**Prof Luca Viganò, Head of CYS Group**

Viganò is the most senior cybersecurity researcher in the department and the natural first-choice primary supervisor. His research on automated security protocol analysis, formal methods for security testing, and the "Explainable Security" (XSec) paradigm, which proposes making AI security decisions transparent and interpretable, aligns directly with the challenge of explaining AI-assisted penetration test findings. He organised the SECTEST workshop series on security testing at ICST conferences and has supervised numerous PhD theses in security verification. His EPSRC-funded projects often involve collaborative supervision with other CYS staff. His 2025 publication with Fournet and Moedersheim in the Journal of Computer Security demonstrates continued active publishing. As group head, he provides strategic connections to the wider King's Cybersecurity Centre and NCSC networks.

**Dr Karine Even-Mendoza, Lecturer, Security Hub member**

Even-Mendoza's expertise in automated testing via fuzzing and LLM-based test generation is the closest methodological match to AI-assisted penetration testing currently at KCL. Her 2025 work on "ReFuzzer" uses large language models in a feedback loop to systematically generate, validate, and refine test inputs for vulnerability discovery, which is a technique directly transferable to automated exploit generation. Her KCL PURE research fingerprint centres on Large Language Models (100%) and Fuzzing (51%). She could provide strong technical co-supervision on AI/ML methodology, LLM-based security tool development, and integration with testing frameworks.

**Dr Nicola Paoletti, Senior Lecturer, Security Hub member**

Paoletti brings deep reinforcement learning expertise that is directly relevant to RL-based autonomous pentesting agents. He co-authored "DRMD: Deep Reinforcement Learning for Malware Detection under Concept Drift" (AAAI 2026, with Pierazzi and Mavroudis), and his broader work on AI safety, adversarial neural network robustness, and detecting misaligned LLM behaviours (funded by Open Philanthropy) all sit within the same research space. His PURE fingerprint shows Deep Reinforcement Learning at 100%. He could supervise the RL components of an autonomous pentesting agent, and his formal verification background could help establish correctness guarantees for any tool that gets built.

**Prof Jose Such, Director, King's Cybersecurity Centre**

As Centre Director, Such provides both AI+security expertise and institutional leadership. He is PI on the EPSRC-funded SAIS (Secure AI Assistants) project (~£1.5M) and supervises PhD students working on adversarial ML for security. While his personal focus leans toward human-centred AI security, his breadth of knowledge, role as Centre Director, and track record of securing major grants make him a strong secondary supervisor who could provide strategic direction, funding opportunities, and external engagement.

### 5.3 Notable Departure

**Dr Fabio Pierazzi** has moved to UCL as Associate Professor. His work on DRL for offensive security, including "Wendigo" (DRL for denial-of-service query discovery, IEEE DLSP 2024) and the "SoK: Pitfalls of Deep Reinforcement Learning for Cybersecurity" (2026), would have made him the single most relevant supervisor. His KCL PhD student Shae McFadden continues publishing on DRL for cybersecurity through KCL PURE. Cross-institutional co-supervision may be possible but should not be assumed.

### 5.4 Other Relevant Staff

**Dr Jie M. Zhang** (Lecturer) works on LLMs for automated software testing, vulnerability detection, and mutation testing, and won the 2025 ACM SIGSOFT Early Career Researcher Award. Her work on LLM-based code generation security (TOSEM 2025) and backdoor attacks for code models (IEEE TSE 2024) is directly relevant to AI-assisted security testing methodologies.

---

## 6. Individual Project (33.3% of Degree)

### 6.1 Structure and Timeline

The 60-credit Individual Project represents approximately 600 hours of work. The programme runs a structured proposal process through the Informatics Project Proposal (IPP) taught module in Semester 2 (January to April), during which students work with an allocated supervisor to develop a formal project proposal.

| Stage             | When            | What                                                  |
| :---------------- | :-------------- | :---------------------------------------------------- |
| Topic exploration | Autumn semester | Browse staff research interests, attend project talks |
| IPP module        | Spring semester | Develop formal proposal with allocated supervisor     |
| Project execution | May – Sep 2027  | Build artefact, run experiments, write dissertation   |
| Submission        | September 2027  | Final dissertation + artefact                         |

Topic selection follows one of three routes: choosing from a staff-proposed list, proposing your own topic with a willing supervisor, or working with an external partner through the Knowledge Exchange Projects (KEPs) scheme. The department handles supervisor allocation, though student preferences are taken into account.

### 6.2 Past Dissertations

KCL's Pure repository only hosts doctoral-level theses from the CYS group, and MSc dissertations are not routinely published in open repositories, on GitHub, or on KEATS. This is standard practice for UK MSc programmes. Recent PhD theses from the CYS group include work by De Pasquale (2025, supervised by Viganò), Castagna (2023, security reasoning, supervised by McBurney & Viganò), and Edu (2022, online security threats, supervised by Such & Suarez-Tangil).

### 6.3 The AI-Assisted Penetration Testing Gap at King's

No published research from KCL specifically addresses AI-assisted penetration testing, which represents a genuine gap and therefore an opportunity for an original contribution. The closest existing work spans three converging threads:

Viganò's Explainable Security (XSec) paradigm for making AI security decisions interpretable. Even-Mendoza's LLM-based fuzzing work (ReFuzzer, 2025) on automated vulnerability discovery. Jie Zhang's research on LLMs for software testing, mutation testing, and code security (TOSEM 2025, IEEE TSE 2024).

Externally, key anchor papers for a literature review include the SoK on pitfalls of DRL for cybersecurity (2026, co-authored by former KCL staff Pierazzi), the METATRON open-source AI pentesting assistant using local LLMs (2025), and Hadi & Al-Saedi's NextGen-PenTest model using Random Forest classifiers (2025).

A project positioned at the intersection of LLM-based automated testing (drawing on Even-Mendoza's methods) and offensive security (drawing on the CYS group's ethical hacking interests) would bridge an existing gap while remaining anchored in active KCL research strengths. Beginning a literature review around these papers now means that when the IPP module opens in January, the proposal arrives close to ready rather than starting from scratch.

---

## 7. NCSC Certification and ACE-CSR

### 7.1 What Certification Requires

The NCSC certifies Master's programmes against the Cyber Security Body of Knowledge (CyBOK), which defines 21 Knowledge Areas across five categories: Human/Organisational/Regulatory Aspects, Attacks & Defences, Systems Security, Software & Platform Security, and Infrastructure Security. For certification, at least 84 taught credits must map to CyBOK Knowledge Areas, and a research dissertation of 40 to 80 credits is required. Applications are assessed by a panel of NCSC, government, industry, and academic representatives, with each application independently graded by at least three panel members.

KCL's on-campus MSc Cyber Security holds full certification valid until 30 September 2026, and the online MSc Advanced Cyber Security is certified until 30 September 2029.

### 7.2 What It Provides in Practice

Graduates of fully certified programmes receive an additional NCSC certificate alongside their degree, which is designed to help employers distinguish qualification quality. This is a quality signal rather than a gateway, as no specific named graduate schemes formally require NCSC-certified degree holders. GCHQ and Civil Service recruitment value the certification as a differentiator but do not make it a formal prerequisite. Industry employers in government, defence, and financial services informally prioritise candidates from certified programmes.

NCSC's own documentation states explicitly that "there will be no funding associated with successful certification," so the certification itself does not unlock bursaries or stipends.

### 7.3 CyberFirst Has No Postgraduate Component

The CyberFirst bursary (£4,000/year plus paid summer placements) is available only to undergraduate students with at least two years of study remaining, which means one-year MSc students are ineligible. The bursary has closed for new applications and is being transferred to the Department for Science, Innovation and Technology under a new "TechFirst" programme. The NCSC does fund PhD studentships through Centres for Doctoral Training at Oxford, UCL, Royal Holloway, and Bristol, but no taught Master's-specific bursary exists.

### 7.4 ACE-CSR in Practice

The ACE-CSR designation, jointly awarded by NCSC and EPSRC to 21 universities nationally, recognises research excellence rather than teaching quality. Each ACE-CSR institution receives approximately £20,000 per year from EPSRC for engagement activities. The practical benefits are access to a collaborative network of leading cybersecurity research groups, facilitated engagement with government organisations and intelligence agencies, enhanced credibility for grant applications, and a signal to industry partners.

King's Cybersecurity Centre uses this status across four research themes: AI Cyber Security, Human-Centred Cyber Security, Formal Cyber Security, and Strategic Cyber Security, drawing on staff from Informatics, War Studies, Defence Studies, and the Policy Institute.

---

## 8. Foundational Reading

### 8.1 Texts Available for Free

**Security Engineering:** Ross Anderson, _Security Engineering: A Guide to Building Dependable Distributed Systems_ (3rd edition, 2020). The entire book is available as free chapter PDFs from the author's Cambridge website at cl.cam.ac.uk/archive/rja14/book.html. All 29 chapters plus teaching videos are available, and this is the single most useful pre-arrival text across the programme.

**Distributed Ledgers:** Narayanan et al., _Bitcoin and Cryptocurrency Technologies_ (Princeton, 2016). A free pre-publication draft PDF is available at bitcoinbook.cs.princeton.edu, with a free Coursera companion course. Antonopoulos's _Mastering Bitcoin_ (3rd edition) is also fully open-source on GitHub.

**Cryptography (reference):** Menezes, van Oorschot & Vanstone, _Handbook of Applied Cryptography_ (1996). Free in full from cacr.uwaterloo.ca/hac/. While dated, the mathematical foundations remain valid and the book is still cited as a primary reference.

**Security Testing:** The OWASP Web Security Testing Guide v4.2 is free at owasp.org, and PortSwigger Web Security Academy (portswigger.net/web-security) provides free interactive labs covering all major web vulnerabilities. Between the two, this is effectively a continuously updated substitute for any printed textbook.

**Security Management:** The NIST Cybersecurity Framework 2.0, SP 800-53 (Security Controls), and SP 800-37 (Risk Management Framework) are all freely available from nist.gov and together cover the governance and risk management frameworks relevant to this module.

**Cross-cutting reference:** The CyBOK (Cyber Security Body of Knowledge) at cybok.org is a free, NCSC-sponsored knowledge base directly aligned with the programme's certification and worth bookmarking as a lookup resource.

### 8.2 Texts Requiring Purchase

| Subject                | Primary Text                                                       | Approx. Cost |
| :--------------------- | :----------------------------------------------------------------- | :----------- |
| Cryptography (primary) | Katz & Lindell, _Introduction to Modern Cryptography_, 3rd Ed.     | ~£50–55      |
| Network Security       | Stallings, _Cryptography and Network Security_, 7th Ed.            | ~£50–65      |
| Digital Forensics      | Carrier, _File System Forensic Analysis_                           | ~£40–55      |
| Security Testing       | Stuttard & Pinto, _The Web Application Hacker's Handbook_, 2nd Ed. | ~£25–35      |
| Security Management    | Whitman & Mattord, _Management of Information Security_, 6th Ed.   | ~£50–80      |
| Software Testing       | Ammann & Offutt, _Introduction to Software Testing_, 2nd Ed.       | ~£50–60      |

The minimum viable pre-arrival spend is approximately £140–175 for the three texts with no strong free alternatives: Katz & Lindell, Carrier, and Ammann & Offutt (if taking the Software Measurement optional). As a registered KCL student, O'Reilly Learning (Safari Books Online) through the KCL Library will likely carry digital versions of several of these at no additional cost, so check library.kcl.ac.uk before purchasing.

---

## 9. Community and Cohort

### 9.1 Societies and Channels

The **KCL Cyber Security Society (KCSS)** is the primary community, with a Discord server (~430 members) accessible via discord.com/invite/aRQETvq22Z. The society runs weekly workshops, guest talks, CTF competitions (including "kingsCTF{}" and HackKing's), and social events. Membership is free. They are active on Instagram (@kclcybersociety, 833+ followers), Facebook, LinkedIn, and X/Twitter.

The **KCL Tech Society** is also relevant, hosting TechSummit (described as the UK's biggest student tech career fair) and multiple hackathons.

No dedicated Slack workspace or formal WhatsApp group was found publicly. MSc cohort WhatsApp groups typically form organically among offer holders closer to September. The official **Welcome to King's** app becomes available from mid-August.

### 9.2 Welcome and Induction

Welcome Week is expected around 21 to 25 September 2026 based on the established pattern. Week 1 is primarily online orientation, and Week 2 involves on-campus mandatory faculty and department induction sessions. The KCLSU Welcome Fair features 300+ student groups and specifically highlights postgraduate engagement.

Enrolment details are sent approximately four weeks before the course start date (mid-August). KCL does not permit deferrals for PGT courses from 2025/26 or 2026/27, so students who want to defer must decline their offer entirely and reapply.

### 9.3 Cohort Profile

The programme has an offer rate of approximately 23% (2023/24 FOI data), which means roughly 1 in 4 applicants receive offers. The cohort likely ranges from 30 to 60 students based on typical KCL MSc programme sizes. The NCSC certification and central London location attract a mix of recent computer science graduates and some industry professionals. No public evidence of GCHQ-sponsored students was found, though the CYS group's stated collaboration with government and law-enforcement agencies makes some government-connected students plausible.

---
