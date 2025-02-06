import boto3
import datetime

def check_iam_activity():
    """Check IAM user activity for anomalies."""
    iam = boto3.client('iam')
    users = iam.list_users()
    for user in users['Users']:
        username = user['UserName']
        print(f"Checking activity for user: {username}")
        
        # Simulate anomaly detection with last access keys usage
        keys = iam.list_access_keys(UserName=username)
        for key in keys['AccessKeyMetadata']:
            last_used = key.get('CreateDate', datetime.datetime.now())
            days_since_used = (datetime.datetime.now() - last_used.replace(tzinfo=None)).days
            if days_since_used > 90:
                print(f"[ALERT] {username} has an old access key that hasn't been used in {days_since_used} days!")

if __name__ == "__main__":
    check_iam_activity()
