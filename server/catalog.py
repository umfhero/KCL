"""Module facts from the supplied registration record, snapshot 5 September 2026.
Preparation topics are suggestions, not a current official weekly syllabus.
"""
MODULES = [
 dict(id='7CCSMCIS',name='Cryptography',term=1,level=7,credits=15,occurrence='000001',description='Understand the mathematics behind secure communication.',assessment='100% two-hour written examination',topics=['Modular arithmetic','Multiplicative inverses','Symmetric encryption','Public-key cryptography','Authentication and signatures'],next='Modular arithmetic',icon='KeyRound'),
 dict(id='7CCSMSEM',name='Security Management',term=1,level=7,credits=15,occurrence='000001',description='Connect technical decisions to risk and organisational needs.',assessment='30% group video; 70% two-hour examination',topics=['Risk and assets','Threat assessment','Security governance','Incident response'],next='Risk and assets',icon='ShieldCheck'),
 dict(id='7CCSMSEN',name='Security Engineering',term=1,level=7,credits=15,occurrence='000001',description='Explore how systems fail and how to design them securely.',assessment='Confirm in the current module handbook',topics=['C and memory','Pointers and the stack','Memory safety','Threat modelling'],next='C and memory',icon='Blocks'),
 dict(id='6CCSARDM',name='Agent Reasoning and Decision Making',term=1,level=6,credits=15,occurrence='000001',description='Study how autonomous agents reason, choose actions and interact.',assessment='Confirm in the current module handbook',topics=['Agents, beliefs and goals','Symbolic reasoning','Decision theory and utility','Argumentation','Multi-agent interaction'],next='Agents, beliefs and goals',icon='Brain',elective=True),
 dict(id='7CCSMCFC',name='Computer Forensics and Cybercrime',term=2,level=7,credits=15,occurrence='000001',description='Follow digital evidence from collection to interpretation.',assessment='100% 3,000-word dissertation',topics=['Digital evidence','Chain of custody','Network forensics','Cybercrime and law'],next='Digital evidence',icon='Fingerprint'),
 dict(id='7CCSMNSE',name='Network Security',term=2,level=7,credits=15,occurrence='000001',description='Bring cryptography and protocols together across networks.',assessment='Confirm in the current module handbook',topics=['TCP/IP foundations','Protocol security','Authentication','Network defence'],next='TCP/IP foundations',icon='Network'),
 dict(id='7CCSMSCT',name='Security Testing',term=2,level=7,credits=15,occurrence='000001',description='Learn to investigate weaknesses and evaluate mitigations.',assessment='Confirm in the current module handbook',topics=['HTTP and sessions','Testing methodology','Web vulnerabilities','Reporting findings'],next='HTTP and sessions',icon='ScanLine'),
 dict(id='7CCSMBDT',name='Big Data Technologies',term=2,level=7,credits=15,occurrence='000001',description='Explore the systems and methods used to process data at scale.',assessment='Confirm in the current module handbook',topics=['Distributed data systems','Data processing models','Scalable storage','Analytics pipelines','Reliability at scale'],next='Distributed data systems',icon='Database',elective=True),
 dict(id='7CCSMPRJ',name='MSc Individual Project',term=3,level=7,credits=60,occurrence='000001',description='Develop a research question and your own technical contribution.',assessment='Dissertation; current milestones to be confirmed',topics=['Research question','Literature and methods','Implementation or analysis','Evaluation','Writing and presentation'],next='Research question',icon='NotebookPen'),
]
ELECTIVES = {
 '1':[{'id':'7CCSMASE','name':'Software Measurement and Testing'},{'id':'7CCEMWNT','name':'Wireless Networks'},{'id':'6CCSARDM','name':'Agent Reasoning and Decision Making'},{'id':'6CCS3VER','name':'Formal Verification'}],
 '2':[{'id':'7CCSMBDT','name':'Big Data Technologies'},{'id':'7CCSMDLC','name':'Distributed Ledgers and Crypto-currencies'},{'id':'6CCS3ML1','name':'Machine Learning'}]
}
READINGS = {
 '7CCSMCIS':[('Handbook of Applied Cryptography','https://cacr.uwaterloo.ca/hac/','Open author-hosted chapters'),('Understanding Cryptography','https://www.crypto-textbook.com/','Companion website; add an authorised book copy')],
 '7CCSMSEN':[('Security Engineering, third edition','https://www.cl.cam.ac.uk/archive/rja14/book.html','Author-hosted reading')],
 '7CCSMSCT':[('OWASP Web Security Testing Guide','https://owasp.org/www-project-web-security-testing-guide/','Open reference'),('PortSwigger Web Security Academy','https://portswigger.net/web-security','Interactive external exercises')],
 '7CCSMSEM':[('NIST Cybersecurity Framework','https://www.nist.gov/cyberframework','Open reference')],
}
DATES=[('2026-09-08','Module record deadline','13:00. Your record totals 180 credits; verify it in the portal.'),('2026-09-28','Semester 1 teaching begins','Course-guide calendar; use your personal timetable.'),('2026-11-02','Semester 1 reading week','2 to 6 November'),('2027-01-11','Assessment period 1','11 to 22 January; individual exams to be confirmed.'),('2027-01-25','Semester 2 teaching begins','Course-guide calendar'),('2027-03-01','Semester 2 reading week','1 to 5 March')]
PRIMER='''# Modular arithmetic and RSA: preparation notes

These locally authored preparation notes support the interactive example. They are not official KCL teaching material. Verify against the module's assigned readings.

## Modular arithmetic
Working modulo n groups integers by the remainder after division by n. For example, 29 mod 12 = 5. Two numbers are congruent modulo n if their difference is divisible by n. Modular arithmetic appears throughout cryptography because calculations can operate in finite sets with useful algebraic properties.

## Multiplicative inverses
The multiplicative inverse of a modulo n is an integer b for which a*b mod n = 1. An inverse exists precisely when gcd(a,n)=1. The inverse of 7 modulo 26 is 15 because 7*15=105 and 105 mod 26=1. The Extended Euclidean Algorithm computes coefficients x and y with a*x+n*y=gcd(a,n); when the gcd is 1, x modulo n is the inverse.

## Toy RSA example
Choose p=5 and q=11. Then n=p*q=55 and phi(n)=(p-1)*(q-1)=40. Select e=3, which is coprime to 40. The private exponent d=27 because 3*27 mod 40=1. For message m=7, c=m^e mod n=13. Decrypting gives c^d mod n=7. The public key is (n,e); the private exponent must be kept secret.

## Connecting the ideas
Prime numbers define n and phi(n). A multiplicative inverse connects the public exponent to the private exponent. Modular exponentiation performs encryption and decryption in this toy construction. Learning inverses first makes the relationship between the keys easier to understand.

## Limits of this example
The tiny primes and raw textbook RSA here are only for learning. Secure real-world encryption needs suitable key sizes, padding and careful implementations. Modern TLS should not be explained as merely sending a message through this toy example: its protocol, key agreement and authentication have distinct roles. Use the current Network Security syllabus and protocol specifications when studying TLS.
'''
