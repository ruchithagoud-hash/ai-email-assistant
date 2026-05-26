from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

TOKEN_PATH = "token.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_unread_emails(max_results=5):
    """Fetch unread emails with subject + snippet."""
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError("token.json not found. Please authenticate Gmail first.")

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(
        userId='me', labelIds=['UNREAD'], maxResults=max_results
    ).execute()

    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']

        sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        snippet = msg_data.get('snippet', '')

        email_list.append({
            "id": msg['id'],
            "from": sender,
            "subject": subject,
            "snippet": snippet
        })

    return email_list

def add_label_to_email(service, msg_id, label_id):
    """Apply a Gmail label to an email."""
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={"addLabelIds": [label_id]}
    ).execute()
