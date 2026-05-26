from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
from datetime import datetime

TOKEN_PATH = "token.json"
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send'
]

# Label IDs for your Gmail (replace with your real ones from get_labels.py)
LABEL_IDS = {
    "Important-General": "Label_2185393708610698481",
    "Important-Urgent": "Label_968871306440364973"
}

def get_important_emails():
    """Fetch important emails based on labels."""
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError("token.json not found. Please authenticate Gmail first.")

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    email_summary = []

    for label_name, label_id in LABEL_IDS.items():
        results = service.users().messages().list(
            userId='me', labelIds=[label_id], maxResults=10
        ).execute()

        messages = results.get('messages', [])
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_data['payload']['headers']
            sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
            email_summary.append(f"{label_name} → {sender} : {subject}")

    return email_summary


def send_reminder_email(email_list):
    """Send the reminder email to yourself."""
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    from email.mime.text import MIMEText
    import base64

    body = "📌 Daily Important Email Reminder:\n\n" + "\n".join(email_list)

    message = MIMEText(body)
    message['to'] = "ruchithaarelli05@gmail.com"  # Replace with your Gmail
    message['subject'] = f"Daily Email Summary - {datetime.now().strftime('%Y-%m-%d')}"
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(userId='me', body={'raw': raw}).execute()
    print("✅ Reminder email sent!")


if __name__ == "__main__":
    emails = get_important_emails()
    if emails:
        send_reminder_email(emails)
    else:
        print("No important emails found today.")
