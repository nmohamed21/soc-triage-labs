# 🛡️ SOC Triage Labs

This repository contains hands-on **Security Operations Center (SOC) triage labs** demonstrating alert analysis, log correlation, and incident response workflows commonly used in blue team environments.

The labs focus on realistic detection and investigation scenarios, emphasizing how analysts validate alerts, correlate multiple data sources, and document findings using standard SOC methodologies.

---

## 🧪 Lab 01 – Authentication Log Triage

Performed Python-based analysis of authentication logs to identify potential brute-force login activity by correlating failed authentication events across multiple users and source IP addresses.

**Key activities:**
- Parsed authentication logs using Python
- Correlated failed login attempts across accounts and IP addresses
- Identified brute-force attack patterns
- Documented findings using SOC triage methodology

---

## 🧪 Lab 02 – Network Traffic Triage

Analyzed suspicious network traffic to identify indicators of lateral movement and reconnaissance activity.

**Key activities:**
- Analyzed SMB and RPC traffic using packet-level inspection
- Identified indicators of potential lateral movement
- Detected SAMR-based account enumeration activity
- Documented findings using SOC incident response and triage workflows

---

## 🧪 Lab 03 – SIEM Alert Triage

Configured and validated SIEM-based detections using **Wazuh** to analyze authentication-related security alerts.

**Key activities:**
- Configured Wazuh to detect Windows-style authentication failures
- Performed alert triage and validation
- Correlated multiple security events
- Documented alerts following standard SOC investigation workflows

---

## 🧪 Lab 04 – File Integrity Monitoring (Wazuh FIM)

Implemented and validated **File Integrity Monitoring (FIM)** using **Wazuh syscheck** to detect unauthorized file system changes and correlate them with user activity and privilege escalation.

This lab demonstrates how SOC analysts investigate file modification alerts and determine whether changes are benign or security-relevant.

**Key activities:**
- Configured Wazuh syscheck to monitor critical directories (`/tmp`, `/etc`)
- Generated file creation, modification, and deletion events
- Detected file activity correlated with privileged command execution (`sudo`)
- Analyzed alert context including user attribution, executed commands, and privilege escalation
- Validated alerts using Wazuh logs and dashboard

**SOC relevance:**
- Demonstrates how file integrity events are rarely standalone
- Shows correlation between file changes and command execution
- Mirrors real-world investigations of insider threats and persistence mechanisms

---

## 🧰 Tools Used

- Python
- Wireshark
- Wazuh SIEM
- Linux system logs
- Windows authentication-style logs

---

## 🧠 Skills Demonstrated

- SOC alert triage and prioritization
- Log analysis and event correlation
- Network traffic analysis
- SIEM-based detection and investigation
- File integrity monitoring and validation
- Threat hunting fundamentals
- Incident investigation and reporting
- SOC investigation workflows

---

## 🎯 Project Goal

The goal of this project is to demonstrate **practical SOC analyst skills** through realistic lab scenarios that go beyond tool configuration and focus on analysis, context, and decision-making.

This repository is intended to reflect the type of investigations performed in Security Operations Centers and to serve as a portfolio of applied blue team experience.
