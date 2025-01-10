🌐 Honeypots in Action: Analyzing Attacks and Strengthening Defenses
👋 Introduction
This project is all about honeypots 🕸️—fake systems designed to attract hackers. By studying how attackers interact with these decoys, we can learn their tricks and build better defenses.

We used three honeypots: Dionaea, Cowrie, and HoneyD. To keep them secure during attacks, we added extra protections using AppArmor 🛡️ and Seccomp 🔒. Together, these tools helped us safely collect data and understand how cybercriminals think.

🎯 Objectives
Here’s what we wanted to achieve:

🕵️‍♂️ Study Hackers: Simulate attacks and learn from them.
🛡️ Stay Secure: Use AppArmor and Seccomp to protect the honeypots.
📊 Visualize Data: Turn the collected data into clear charts using the ELK Stack.
🛠️ Honeypots Overview
Here’s how each honeypot works:

Dionaea 🐙: Captures malware to study how it spreads.
Cowrie 🐚: Logs every command attackers type in a fake shell environment.
HoneyD 🐝: Simulates a network of devices to trick hackers.
These honeypots helped us simulate real-world attacks, like password guessing and malware injections, in a safe way.

🔐 Security Concepts: AppArmor & Seccomp
To make sure our honeypots couldn’t be turned against us, we used these security tools:

AppArmor 🛡️: Sets strict rules for what each honeypot is allowed to do, like letting Dionaea capture traffic but blocking access to sensitive files.
Seccomp 🔒: Limits the actions honeypots can perform, so even if hacked, they’re restricted to doing only harmless tasks.
🌟 Why This Project Matters
Honeypots show us how hackers work, letting us stay one step ahead. By adding tools like AppArmor and Seccomp, we kept the honeypots secure while gaining valuable insights. This project proves that small, smart steps can make a big difference in cybersecurity.

