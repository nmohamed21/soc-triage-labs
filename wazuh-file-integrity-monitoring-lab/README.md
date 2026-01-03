# 🛡️ Wazuh File Integrity Monitoring (FIM) Lab

## Overview
This repository documents a hands-on lab validating **File Integrity Monitoring (FIM)** using **Wazuh**. The lab demonstrates monitoring of critical directories, detection of file creation/modification/deletion, and correlation with user activity and privilege escalation.

## Lab Objectives
- Configure Wazuh syscheck (FIM)
- Monitor `/tmp` and `/etc`
- Generate file integrity events
- Validate alerts via CLI and Wazuh Dashboard
- Analyze alert context (user, command, privilege escalation)

## Environment
- Wazuh 4.x
- Ubuntu Linux Agent
- Agent Name: bob-VMware-Virtual-Platform

## Configuration
Syscheck was enabled in `/var/ossec/etc/ossec.conf` and the agent restarted.

## Simulation
File changes were generated using:
```bash
echo "test" | sudo tee /tmp/fim_test.txt
echo "change" | sudo tee -a /tmp/fim_test.txt
sudo rm /tmp/fim_test.txt
```

## Detection
Alerts captured include:
- File path: `/tmp/fim_test.txt`
- Command execution via `sudo`
- User attribution and privilege escalation
- Log source: journald

## Screenshots
See the `screenshots/` directory for:
- Agent status
- Syscheck configuration
- File activity commands
- Wazuh alert evidence (CLI + Dashboard)

## Conclusion
This lab confirms that Wazuh successfully detects and correlates file integrity events with user actions, providing SOC-relevant visibility into system changes.

## Repo Structure
```
wazuh-file-integrity-monitoring-lab/
├── README.md
├── screenshots/
```
