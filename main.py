from gmail_reader import get_unread_emails, add_label_to_email
from classify import classify_email
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

# Label IDs from get_labels.py output
LABEL_IDS = {
    "Important-General": "Label_2185393708610698481",
    "Important-Urgent": "Label_968871306440364973",
    "Personals": "Label_369978338867377434",
    "Works": "Label_9015605077310858516",
    "SPAM": "SPAM"
}

TOKEN_PATH = "token.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Gmail API service
if not os.path.exists(TOKEN_PATH):
    raise FileNotFoundError("token.json not found. Please authenticate Gmail first.")

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
service = build('gmail', 'v1', credentials=creds)

# Fetch emails
emails = get_unread_emails()

for email in emails:
    subject = email.get("subject", "No Subject")
    snippet = email.get("snippet", "")

    classification = classify_email(subject, snippet)

    print(f"From: {email['from']}")
    print(f"Subject: {subject}")
    print(f"Classification: {classification}")

    label_id = LABEL_IDS.get(classification)

    if label_id:
        try:
            add_label_to_email(service, email["id"], label_id)
            print(f"✅ Applied label: {classification}")
        except Exception as e:
            print(f"⚠️ Failed to apply label: {e}")