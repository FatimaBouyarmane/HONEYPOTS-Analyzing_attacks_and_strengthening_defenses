# 🌐 Honeypots in Action: Analyzing Attacks and Strengthening Defenses

## 👋 Introduction  
This project explores **honeypots** 🕸️—fake systems designed to attract hackers. By studying how attackers interact with these decoys, we can learn their tricks and build better defenses.

We used three honeypots: **Dionaea**, **Cowrie**, and **HoneyD**. To keep them secure during attacks, we added extra protections using **AppArmor** 🛡️ and **Seccomp** 🔒. Together, these tools helped us safely collect data and understand how cybercriminals think.

---

## 🎯 Objectives  
Our project had three main goals:  
1. 🕵️‍♂️ **Study Hackers**: Simulate attacks and learn their techniques.  
2. 🛡️ **Stay Secure**: Use AppArmor and Seccomp to protect the honeypots.  
3. 📊 **Visualize Data**: Turn the collected data into clear charts using the **ELK Stack**.

---

## 🛠️ Honeypots Overview  
Here’s how the honeypots worked:  

- **Dionaea** 🐙: Captures malware to study how it spreads.  
- **Cowrie** 🐚: Logs every command attackers type in a fake shell environment.  
- **HoneyD** 🐝: Simulates a network of devices to trick hackers.  

These honeypots allowed us to safely simulate real-world attacks, like password brute-forcing and malware injections.

---

## 🔐 Security Concepts: AppArmor & Seccomp  

### 🛡️ AppArmor  
AppArmor sets strict rules for what each honeypot can do. For example, Dionaea could capture network traffic but was blocked from accessing sensitive files.  

### 🔒 Seccomp  
Seccomp limits what actions honeypots can perform. Even if a hacker breached one, they’d be restricted to harmless tasks, thanks to these controls.

---

## 🌟 Why This Project Matters  
Honeypots help us understand how hackers work, letting us stay one step ahead. With added tools like AppArmor and Seccomp, this project demonstrates how small, smart measures can greatly enhance cybersecurity.

---
