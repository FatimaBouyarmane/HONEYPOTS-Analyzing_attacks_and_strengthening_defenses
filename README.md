# 🌐 **Honeypots in Action: Analyzing Attacks and Strengthening Defenses**

---

## 👋 **Introduction**

Welcome to **Honeypots in Action**! This project is all about using **honeypots** 🕸️—decoy systems that trick hackers into attacking fake targets. Why? Because by observing their behavior, we can learn their tactics, tools, and strategies, and build stronger defenses.

We set up three honeypots: **Dionaea**, **Cowrie**, and **HoneyD**. To ensure they stayed safe while under attack, we added extra security layers with **AppArmor** 🛡️ and **Seccomp** 🔒. Together, they helped us safely collect attack data and gain insights into the minds of cybercriminals.

---

## 🎯 **Objectives**

Here’s what we set out to achieve:

- 🕵️‍♂️ **Understand Attackers**: Simulate real-world cyberattacks to analyze hackers’ methods.  
- 🛡️ **Strengthen Defenses**: Use tools like AppArmor and Seccomp to ensure our honeypots remain secure.  
- 📊 **Visualize the Data**: Create charts and dashboards using the ELK Stack to make sense of the collected attack data.

---

## 🛠️ **Honeypots Overview**

Let’s meet the tools that made it all happen:

- **Dionaea** 🐙: A malware sponge that captures malicious files and helps us study how they spread.  
- **Cowrie** 🐚: A fake command-line shell that logs every command hackers type, giving us a peek into their strategies.  
- **HoneyD** 🐝: The ultimate chameleon—it can mimic an entire network of devices to confuse attackers.

These honeypots let us simulate attack scenarios, such as password brute-forcing and malware injection, in a controlled environment.

---

## 🔐 **Security Concepts: AppArmor & Seccomp**

To ensure our honeypots couldn’t be used against us, we relied on two Linux security tools:

- 🛡️ **AppArmor**  
  Think of AppArmor as a strict set of rules for each honeypot. It says, “Dionaea, you can listen to network traffic, but you’re NOT allowed to access sensitive files.” These rules reduce the honeypots' attack surface, keeping them focused and safe.  

- 🔒 **Seccomp**  
  Seccomp takes security a step further by limiting what actions honeypots can perform. It’s like giving them a small vocabulary—only essential system calls are allowed. Even if a hacker breaches one honeypot, their options are severely restricted.

---
