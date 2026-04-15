# KCL MSc Cyber Security: complete intelligence brief for September 2026 entry

**This report is a comprehensive pre-arrival briefing covering every dimension of the King's College London MSc Cyber Security programme — modules, staff, NCSC certification, reading lists, project planning, community, and Royal Holloway scholarship logistics.** The programme is NCSC-certified (until 30 September 2026, with renewal expected), delivered by the Department of Informatics, and anchored by the Cybersecurity (CYS) research group within King's Cybersecurity Centre, an EPSRC-NCSC Academic Centre of Excellence. What follows is the most actionable intelligence available from public sources across all seven requested sections.

---

## Section 1: Module-by-module intelligence

The MSc comprises **120 taught credits** (six compulsory 15-credit modules plus electives) and a **60-credit Individual Project**. Semesters are split Autumn (September–December) and Spring (January–April), with the project running across both semesters and summer. KCL locks detailed syllabi behind KEATS (its VLE), but the Study Abroad module catalogue, programme pages, and community sources fill most gaps.

### Compulsory modules

**Cryptography — 7CCSMCIS (15 credits, Autumn)**
Assessment is **100% examination**. The module covers number theory foundations (modular arithmetic, Euler's theorem, Extended Euclidean Algorithm, Chinese Remainder Theorem), classical and modern ciphers (DES, AES), public-key cryptosystems (RSA, ElGamal), key-establishment protocols (Diffie-Hellman, Needham-Schroeder, Kerberos), digital signatures (RSA, ElGamal, DSA), and zero-knowledge protocols (Fiat-Shamir). This is the mathematical backbone of the programme and a **prerequisite for Network Security and Computer Forensics**. Prior knowledge of discrete mathematics and modular arithmetic is strongly recommended. Formerly taught by Prof Luca Viganò (2014–2021); the current lecturer may differ. Student feedback from the online variant notes the compressed format can feel rushed for such mathematically dense content.

**Security Engineering — 7CCSMSEN (15 credits, Autumn)**
Assessment is **70% examination, 30% coursework**. This is the most technically hands-on Autumn module, covering command injection, x86 assembly, stack-based buffer overflows, shellcode writing, format string vulnerabilities, memory corruption mitigations, secure software development (threat modelling, defence-in-depth), static analysis, and symbolic execution. **Prior experience with C/C++ and basic OS concepts is essential**; students without low-level programming experience will struggle with the exploitation content. The coursework component likely involves practical exploit development or secure code analysis.

**Security Management — 7CCSMSEM (15 credits, Autumn)**
Assessment format is not publicly confirmed but likely includes both examination and coursework (essays/reports). Covers risk assessment and management, security auditing, business continuity planning, cost-effective cybersecurity strategy, risk communication, regulatory frameworks, and security governance. This is the least technical compulsory module and provides the management and policy lens. Prior knowledge of organisational IT structures is helpful but not required. Students from technical backgrounds sometimes find the essay-based assessment style unfamiliar.

**Security Testing — 7CCSMSTE (15 credits, Spring)**
Assessment format is not publicly confirmed; likely a mix of examination and practical coursework. Covers penetration testing methodology, ethical hacking, social engineering, web application attacks, database attacks, system-level attacks, vulnerability assessment, and security testing frameworks. Students learn to **implement and report on penetration tests**, interpret vulnerabilities, and apply mitigation strategies. This is the module most directly relevant to offensive security careers. Networking fundamentals and web application basics are important prerequisites. The KCL virtual lab environment supports hands-on work.

**Network Security — 7CCSMNSE (15 credits, Spring)**
Assessment is likely around **85% examination, 15% coursework** (based on the shared undergraduate module structure). Requires completion of Cryptography as a prerequisite. Covers network fundamentals, security of Internet protocols (wired and wireless), network attacks and countermeasures, and network security protocol evaluation. Student commentary describes the scope as broader than just TCP/UDP — encompassing wireless security, protocol-level attacks, and defence strategies. TCP/IP knowledge from prior study or self-directed learning is strongly recommended.

**Computer Forensics and Cybercrime — 7CCSMCFC (15 credits, Spring)**
Assessment format not publicly confirmed; likely examination plus coursework. Requires Cryptography as a prerequisite. Covers legal aspects of cybersecurity (UK Computer Misuse Act, GDPR, international legislation), forensic techniques and methodologies, incident management, digital evidence handling, and the cybercrime landscape. Forum commentary describes this as covering "investigation and cyber crimes" with real-world scenario application. Prior knowledge of cryptography fundamentals and basic legal awareness is helpful.

**Individual Project — 7CCSMPRJ (60 credits, full year)**
Assessment is **100% project** (dissertation plus artefact). This accounts for one-third of the degree classification weighting. Covered in detail in Section 5 below.

### Optional modules

**Distributed Ledgers and Crypto-Currencies — 7CCSMDLC (15 credits, Spring)**
Assessment not publicly confirmed; likely includes practical coursework elements. Covers applied cryptography for blockchain, peer-to-peer consensus networks, Bitcoin architecture, Ethereum and smart contracts, mechanism design and game theory, permissioned vs permissionless networks, and the CAP theorem. Lecture material is developed by KCL instructors and hosted at blockchain.kcl.ac.uk. Forum commentary from students notes this module feels peripherally related to core cybersecurity but is valuable for career breadth — one commenter observed that mastering distributed ledgers "gives you a world that needs you." **Strong cryptography knowledge is a de facto prerequisite**.

**Software Measurement and Testing — 7CCSMASE (15 credits, Autumn)**
Assessment is **85% examination, 15% coursework**. Covers software lifecycle testing, white-box and black-box testing, finite models (control flow graphs, data-flow graphs, finite state machines), coverage metrics, symbolic execution, static analysis, test oracles, and automated test data generation. This is an analytically rigorous module focused on software quality assurance rather than security testing per se. Programming experience and basic algorithms knowledge are recommended. The module shares teaching methods with the Software Systems group.

### Assessment pattern summary

| Module               | Code     | Credits | Semester  | Assessment             |
| -------------------- | -------- | ------- | --------- | ---------------------- |
| Cryptography         | 7CCSMCIS | 15      | Autumn    | 100% Exam              |
| Security Engineering | 7CCSMSEN | 15      | Autumn    | 70% Exam / 30% CW      |
| Security Management  | 7CCSMSEM | 15      | Autumn    | Not publicly confirmed |
| Security Testing     | 7CCSMSTE | 15      | Spring    | Not publicly confirmed |
| Network Security     | 7CCSMNSE | 15      | Spring    | ~85% Exam / ~15% CW    |
| Computer Forensics   | 7CCSMCFC | 15      | Spring    | Not publicly confirmed |
| Individual Project   | 7CCSMPRJ | 60      | Full year | 100% Project           |
| Distributed Ledgers  | 7CCSMDLC | 15      | Spring    | Not publicly confirmed |
| Software Measurement | 7CCSMASE | 15      | Autumn    | 85% Exam / 15% CW      |

### Community intelligence on modules

No Reddit r/KCL posts specifically discussing the MSc Cyber Security modules were found — the programme is notably under-discussed on Reddit compared to comparable programmes. No past exam papers or coursework briefs were found on GitHub or Scribd; KCL maintains strong academic integrity controls. **The Student Room** is the richest source of student commentary. A verified StudentCrowd reviewer who took both Security Management and Cryptography on the distance-learning variant criticised compressed teaching timelines (6 weeks per module) and limited contact hours (1 hour/week). This criticism applies primarily to the online variant; the on-campus programme has substantially more contact time. No Rate My Professors reviews exist for specific cybersecurity lecturers.

---

## Section 2: Department of Informatics staff and research mapping

### Research groups and centres

The department houses three overlapping cybersecurity entities. The **Cybersecurity (CYS) Group** is the core research group, led by Prof Luca Viganò (Head) and Dr Ruba Abu-Salma (Deputy Head), with themes spanning AI/ML for cybersecurity, verification and testing, and human factors. The **Security Hub** is a cross-cutting coordination mechanism within Informatics, co-championed by Prof Jose Such and Dr Abu-Salma, with five explicit themes: **AI Cyber Security**, Formal Cyber Security, Strategic Cyber Security, Human-Centred Cyber Security, and interdisciplinary connections. The **King's Cybersecurity Centre** is the university-wide EPSRC-NCSC ACE-CSR entity directed by Prof Such, spanning Informatics, War Studies, Defence Studies, Digital Humanities, and the Policy Institute.

The AI Cyber Security theme within the Security Hub is defined as comprising "both the use of AI for cyber security (including data-driven techniques such as Machine Learning, but also knowledge-based techniques such as Argumentation, Normative Systems, Trust), and the cyber security of AI itself." This is the institutional home for AI-assisted security research.

### Supervisor shortlist for AI-assisted penetration testing

**1. Prof Luca Viganò — Head of CYS Group**
Viganò is the most senior cybersecurity researcher in the department and the natural first-choice primary supervisor. His research on automated security protocol analysis, formal methods for security testing, and the "Explainable Security" (XSec) paradigm — which proposes making AI security decisions transparent and interpretable — aligns directly with the challenge of explaining AI-assisted penetration test findings. He organised the SECTEST workshop series on security testing at ICST conferences and has supervised numerous PhD theses in security verification. His EPSRC-funded projects often involve collaborative supervision with other CYS staff. As group head, he provides strategic connections to the wider King's Cybersecurity Centre and NCSC networks. His 2025 publication with Fournet and Moedersheim in the Journal of Computer Security demonstrates continued active publishing.

**2. Dr Karine Even-Mendoza — Lecturer, Security Hub member**
Even-Mendoza's expertise in automated testing via fuzzing and LLM-based test generation is the closest methodological match to AI-assisted penetration testing currently at KCL. Her 2025 work on "ReFuzzer" uses large language models in a feedback loop to systematically generate, validate, and refine test inputs for vulnerability discovery — a technique directly transferable to automated exploit generation. Her KCL PURE research fingerprint centres on **Large Language Models (100%) and Fuzzing (51%)**. She could provide strong technical co-supervision on AI/ML methodology, LLM-based security tool development, and integration with testing frameworks.

**3. Dr Nicola Paoletti — Senior Lecturer, Security Hub member**
Paoletti brings deep reinforcement learning expertise essential for RL-based autonomous pentesting agents. He co-authored "DRMD: Deep Reinforcement Learning for Malware Detection under Concept Drift" (AAAI 2026, with Pierazzi and Mavroudis), and his broader work on AI safety, adversarial neural network robustness, and detecting misaligned LLM behaviours (funded by Open Philanthropy) is highly relevant. His PURE fingerprint shows **Deep Reinforcement Learning at 100%**. He could supervise the RL components of an autonomous pentesting agent while his formal verification background could help establish correctness guarantees.

**4. Prof Jose Such — Director, King's Cybersecurity Centre**
As Centre Director, Such provides both AI+security expertise and institutional leadership. He is PI on the EPSRC-funded SAIS (Secure AI Assistants) project (~£1.5M) and supervises PhD students working on adversarial ML for security. While his personal focus leans toward human-centred AI security, his breadth of knowledge, role as Centre Director, and track record of securing major grants make him a strong secondary supervisor who could provide strategic direction, funding opportunities, and external engagement.

### Notable departure affecting supervision options

**Dr Fabio Pierazzi** has moved to UCL as Associate Professor. His work on DRL for offensive security — including "Wendigo" (DRL for denial-of-service query discovery, IEEE DLSP 2024) and the "SoK: Pitfalls of Deep Reinforcement Learning for Cybersecurity" (2026) — would have made him the single most relevant supervisor. His KCL PhD student **Shae McFadden** continues publishing on DRL for cybersecurity through KCL PURE. Cross-institutional co-supervision may be possible but should not be assumed.

### Other relevant staff

**Dr Jie M. Zhang** (Lecturer) works on LLMs for automated software testing, vulnerability detection, and mutation testing — winning the 2025 ACM SIGSOFT Early Career Researcher Award. Her work on LLM-based code generation security (TOSEM 2025) and backdoor attacks for code models (IEEE TSE 2024) is directly relevant to AI-assisted security testing methodologies.

---

## Section 3: NCSC certification and ACE-CSR in practice

### What certification requires

NCSC certifies Master's programmes against the **Cyber Security Body of Knowledge (CyBOK)**, which defines 21 Knowledge Areas across five categories: Human/Organisational/Regulatory Aspects, Attacks & Defences, Systems Security, Software & Platform Security, and Infrastructure Security. For certification, **at least 84 taught credits** must map to CyBOK Knowledge Areas, and a **research dissertation of 40–80 credits** is required. Applications are assessed by a panel of NCSC, government, industry, and academic representatives, with each application independently graded by at least three panel members across six areas including taught content, assessment materials, and dissertation quality. KCL's on-campus MSc Cyber Security holds **full certification valid until 30 September 2026**, and the online MSc Advanced Cyber Security is certified until 30 September 2029.

### What certification does and does not provide

Graduates of fully certified programmes receive an **additional NCSC certificate** alongside their degree, designed to help employers distinguish qualification quality. However, the certification is a quality signal, not a gateway — **no specific named graduate schemes formally require NCSC-certified degree holders**. NCSC's own documentation states explicitly that "there will be no funding associated with successful certification." GCHQ and Civil Service recruitment value the certification as a differentiator but do not make it a formal prerequisite. Industry employers in government, defence, and financial services informally prioritise candidates from certified programmes.

### CyberFirst has no postgraduate component

The CyberFirst bursary (£4,000/year plus paid summer placements) is available **only to undergraduate students with at least two years of study remaining**. One-year MSc students are ineligible. The bursary has now **closed for new applications** and is being transferred to the Department for Science, Innovation and Technology under the new "TechFirst" programme. The NCSC does fund PhD studentships through Centres for Doctoral Training at Oxford, UCL, Royal Holloway, and Bristol, but no taught Master's-specific bursary exists.

### ACE-CSR: research credibility and access

The ACE-CSR designation, jointly awarded by NCSC and EPSRC to **21 universities** nationally, recognises research excellence rather than teaching quality. Each ACE-CSR institution receives approximately **£20,000 per year** from EPSRC for engagement activities. The practical benefits are access to a collaborative network of leading cybersecurity research groups, facilitated engagement with government organisations and intelligence agencies, enhanced credibility for grant applications, and a signal to industry partners. King's Cybersecurity Centre leverages this status across four research themes — AI Cyber Security, Human-Centred Cyber Security, Formal Cyber Security, and Strategic Cyber Security — drawing on staff from Informatics, War Studies, Defence Studies, and the Policy Institute.

---

## Section 4: Foundational reading by module area

### Texts available for free

**Security Engineering:** Ross Anderson's _Security Engineering: A Guide to Building Dependable Distributed Systems_ (3rd edition, 2020) is the definitive text and is **entirely free** as chapter PDFs from the author's Cambridge website (cl.cam.ac.uk/archive/rja14/book.html). Bruce Schneier called it "the best book on the topic there is." All 29 chapters plus teaching videos are available.

**Distributed Ledgers:** Narayanan et al., _Bitcoin and Cryptocurrency Technologies_ (Princeton, 2016) has a **free pre-publication draft PDF** at bitcoinbook.cs.princeton.edu, plus a free Coursera companion course. Antonopoulos's _Mastering Bitcoin_ (3rd edition) is also fully open-source on GitHub.

**Cryptography (reference):** Menezes, van Oorschot & Vanstone's _Handbook of Applied Cryptography_ (1996) is **free in full** from cacr.uwaterloo.ca/hac/. While dated, the mathematical foundations remain valid. The American Mathematical Society Bulletin described it as the single most important cryptography reference.

**Security Testing:** The **OWASP Web Security Testing Guide v4.2** is free at owasp.org, and **PortSwigger Web Security Academy** (portswigger.net/web-security) provides free interactive labs covering all major web vulnerabilities — effectively a continuously updated successor to the printed textbook.

**Security Management:** The **NIST Cybersecurity Framework 2.0**, SP 800-53 (Security Controls), and SP 800-37 (Risk Management Framework) are all freely available from nist.gov and together cover the governance and risk management frameworks relevant to this module.

### Texts requiring purchase

| Subject                | Primary Text                                                                  | Approx. Cost (Amazon UK) |
| ---------------------- | ----------------------------------------------------------------------------- | ------------------------ |
| Cryptography (primary) | Katz & Lindell, _Introduction to Modern Cryptography_, Revised 3rd Ed. (2025) | ~£50–55                  |
| Network Security       | Stallings, _Cryptography and Network Security_, 7th Ed. (2017)                | ~£50–65                  |
| Digital Forensics      | Carrier, _File System Forensic Analysis_ (2005)                               | ~£40–55                  |
| Security Testing       | Stuttard & Pinto, _The Web Application Hacker's Handbook_, 2nd Ed. (2011)     | ~£25–35                  |
| Security Management    | Whitman & Mattord, _Management of Information Security_, 6th Ed. (2018)       | ~£50–80                  |
| Software Testing       | Ammann & Offutt, _Introduction to Software Testing_, 2nd Ed. (2017)           | ~£50–60                  |

**Minimum viable pre-arrival spend is approximately £140–175** for the three texts with no strong free alternatives: Katz & Lindell, Carrier, and Ammann & Offutt. All other areas have excellent free resources. As a registered KCL student, O'Reilly Learning (Safari Books Online) through the KCL Library will likely carry digital versions of several of these texts at no additional cost — check library.kcl.ac.uk before purchasing.

The **CyBOK (Cyber Security Body of Knowledge)** at cybok.org is a free, NCSC-sponsored knowledge base directly aligned with the programme's certification and worth reviewing as a cross-cutting reference.

---

## Section 5: Individual project — early direction setting

### Structure and timeline

The 60-credit Individual Project (7CCSMPRJ) represents approximately **600 hours of work** and accounts for one-third of the degree classification weighting. The programme runs a structured proposal process through the **Informatics Project Proposal (IPP)** taught module in Semester 2 (January–April), during which students work with an allocated supervisor to develop a formal project proposal. Topic selection follows one of three routes: choosing from a staff-proposed list, proposing your own topic with a willing supervisor, or working with an external partner through the **Knowledge Exchange Projects (KEPs)** scheme. The department handles supervisor allocation — students are not solely responsible for finding a supervisor, though preferences are considered. The main project execution runs over summer (May–September), with submission typically in September.

### Past dissertations are not publicly available

KCL's Pure repository (kclpure.kcl.ac.uk) only hosts **doctoral-level theses** from the CYS group. MSc dissertations are internal assessments and are not routinely published in open repositories, on GitHub, or on KEATS. This is standard for UK MSc programmes. Recent PhD theses from the CYS group include work by De Pasquale (2025, supervised by Viganò), Castagna (2023, security reasoning, supervised by McBurney & Viganò), and Edu (2022, online security threats, supervised by Such & Suarez-Tangil).

### The AI-assisted penetration testing gap at King's

**No published research from KCL specifically addresses AI-assisted penetration testing.** This represents a genuine opportunity. The closest existing work spans three converging threads: Viganò's Explainable Security (XSec) paradigm for making AI security decisions interpretable; Even-Mendoza's LLM-based fuzzing work (ReFuzzer, 2025) on automated vulnerability discovery; and Jie Zhang's research on LLMs for software testing, mutation testing, and code security (TOSEM 2025, IEEE TSE 2024). Externally, key anchor papers for a literature review include the SoK on pitfalls of DRL for cybersecurity (2026, co-authored by former KCL staff Pierazzi), the METATRON open-source AI pentesting assistant using local LLMs (2025), and Hadi & Al-Saedi's NextGen-PenTest model using Random Forest classifiers (2025).

A project positioned at the intersection of LLM-based automated testing (drawing on Even-Mendoza's methods) and offensive security (drawing on the CYS group's ethical hacking interests) would bridge an existing gap while remaining anchored in active KCL research strengths.

---

## Section 6: Community and cohort profile

### The KCL Cyber Security Society is the primary community

The **KCL Cyber Security Society (KCSS)** is active and KCLSU-affiliated, with a **Discord server (~432 members)** accessible via discord.com/invite/aRQETvq22Z. The society runs weekly workshops, guest talks, CTF competitions (including the "kingsCTF{}" series and HackKing's), and social events. Membership is free. They are active on Instagram (@kclcybersociety, **833+ followers**), Facebook, LinkedIn, and X/Twitter. The **KCL Tech Society** is also relevant, hosting TechSummit (described as the UK's biggest student tech career fair) and multiple hackathons. Joining the KCSS Discord before term starts is the single most useful community action.

No dedicated Slack workspace or formal WhatsApp group was found publicly. MSc cohort WhatsApp groups typically form organically among offer holders closer to September. General KCL freshers Facebook groups and the official **Welcome to King's app** (available from mid-August) are the main pre-arrival channels.

### Welcome and induction

**Welcome Week is expected around 21–25 September 2026** (based on the established pattern). Week 1 is primarily online orientation; Week 2 involves on-campus mandatory faculty and department induction sessions. The KCLSU Welcome Fair features 300+ student groups and specifically highlights postgraduate engagement opportunities. Enrolment details are sent approximately four weeks before course start (mid-August). **KCL does not permit deferrals** for PGT courses from 2025/26 or 2026/27; students wishing to defer must decline their offer entirely.

### Cohort profile

The programme has an **offer rate of approximately 23%** (2023/24 FOI data), making it competitive — roughly 1 in 4 applicants receive offers. Precise cohort size is not publicly available but likely ranges from **30–60 students** based on typical KCL MSc programme sizes. The NCSC certification and central London location attract a mix of fresh computer science graduates and some industry professionals. No public evidence of GCHQ-sponsored students was found, though the CYS group's stated collaboration with government and law-enforcement agencies makes some government-connected students plausible.

---

## Section 7: Royal Holloway scholarship deadlines and the programme name question

### Both deadlines are confirmed as 15 June 2026

The **Professor Mike Walker OBE Scholarship** deadline is **11:59pm UK time on Monday 15 June 2026**. It offers a **tuition fee reduction of up to £12,000** (one award available, open to Home and International students). The **Gent-Rust Scholarship** deadline is the same: **15 June 2026**. It provides a **cash award of £8,000** (two awards available, Home fee status only). Both require a 400-word supporting statement demonstrating financial need; applications exceeding the word count are automatically rejected.

### The programme name discrepancy is real and needs resolution

Royal Holloway's ISG department **renamed the programme in 2026** from "MSc Information Security" to **"MSc Information and Cyber Security"**, stating this reflects "both the historic foundation of this interdisciplinary degree and the diversity of perspectives and careers in this crucial domain for society." However, **the Mike Walker scholarship page still lists "MSc Information Security" as an eligible programme** — this appears to be a legacy reference that has not been updated. The Gent-Rust scholarship lists the "Information Security" department as eligible, which should still apply under the renamed programme. To eliminate any risk of disqualification on a technicality, **contact rhps@rhul.ac.uk before the deadline** to confirm the renamed programme remains eligible for both scholarships.

### Holding both offers simultaneously is permitted

Unlike undergraduate UCAS, **UK postgraduate applications have no firm/insurance system**. Students routinely hold acceptances at multiple institutions simultaneously. There is no legal obligation until formal enrolment at the start of the academic year. Neither the Mike Walker nor Gent-Rust scholarship terms require you to have "firmly accepted" the Royal Holloway offer by the application deadline — you simply need an offer to study one of the eligible courses. The terms state you cannot hold multiple _Royal Holloway_ scholarships simultaneously (the higher-value one is awarded), but say nothing about holding offers at other universities.

**You can hold a KCL acceptance and an RH offer simultaneously, apply for both RH scholarships by 15 June, and defer the final decision until scholarship outcomes are known.** If you win a scholarship but ultimately decline the RH offer, the scholarship simply lapses — the award is contingent on being enrolled at Royal Holloway. Any deposit paid to an institution you ultimately decline may be forfeited, but this is a financial cost, not a contractual prohibition.

---

## Conclusion

The KCL MSc Cyber Security is a rigorous, exam-heavy programme anchored in strong cryptographic and systems security foundations, with the CYS group providing genuine research depth in AI and cybersecurity. **Three immediate actions matter most before September**: join the KCSS Discord to connect with the cohort early; begin reading Anderson's _Security Engineering_ (free) and working through PortSwigger Web Security Academy (free) for Security Testing preparation; and email rhps@rhul.ac.uk to confirm the renamed "MSc Information and Cyber Security" remains eligible for the Mike Walker and Gent-Rust scholarships before the 15 June deadline.

For the Individual Project, the absence of published KCL research specifically on AI-assisted penetration testing is a strategic opportunity rather than a weakness. A project bridging Even-Mendoza's LLM-based automated testing methods with the CYS group's ethical hacking interests — supervised by Viganò as primary and Even-Mendoza or Paoletti as technical co-supervisor — would sit at an active research frontier while remaining grounded in departmental expertise. Begin building a literature review around the 2026 SoK on DRL for cybersecurity, the METATRON LLM pentesting assistant, and Viganò's XSec paradigm now, so that when the IPP module opens in January, you arrive with a proposal-ready concept.
