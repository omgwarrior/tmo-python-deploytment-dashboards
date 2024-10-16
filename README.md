# Splunk HTTP 400 Response Ratio Monitor

This repository contains configuration files for a Splunk dashboard and alert to monitor the ratio of HTTP 400 responses within a 24-hour period. If the ratio exceeds **10:20 (50%)**, an alert is triggered, and notifications are sent via email or Microsoft Teams.

## Files Included
- **dashboard.json**: Configuration for the Splunk dashboard that visualizes the ratio of HTTP 400 responses.
- **alert_config.json**: Configuration for the Splunk alert that sends notifications based on the defined ratio.

---

## Prerequisites
- A **Splunk Enterprise** or **Splunk Cloud** instance.
- A **Splunk API Token** with permission to create dashboards and alerts.
- **Python 3.x** installed on your machine.
- A **Microsoft Teams webhook URL** (if using Teams for notifications).

---

## Python Deployment Setup

### Step 1: Install Required Libraries
Make sure you have the necessary Python libraries installed by running:

```bash
pip install requests
