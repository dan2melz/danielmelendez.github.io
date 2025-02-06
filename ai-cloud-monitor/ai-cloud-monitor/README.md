# AI-Powered Cloud Security Monitor

## Overview
This project scans AWS IAM user activity and detects anomalies in access key usage. It flags unused keys older than 90 days to improve security.

## Installation & Setup
1. Install dependencies:
   ```bash
   pip install boto3
   ```
2. Configure AWS credentials:
   ```bash
   aws configure
   ```
3. Run the script:
   ```bash
   python ai_cloud_monitor.py
   ```

## How It Works
- Retrieves IAM users from AWS.
- Checks access key usage history.
- Flags access keys unused for **90+ days** as potential security risks.

## Example Output
```
Checking activity for user: admin-user
[ALERT] admin-user has an old access key that hasn't been used in 120 days!
```

## Future Enhancements
- Implement **machine learning-based** anomaly detection.
- Add **Slack/SNS notifications** for real-time alerts.
