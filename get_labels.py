from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

TOKEN_PATH = "token.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def list_labels():
    """Fetch and print all Gmail labels with their IDs."""
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError("token.json not found. Please authenticate Gmail first.")

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print("No labels found.")
        return

    for label in labels:
        print(f"{label['name']}  -->  {label['id']}")

if __name__ == "__main__":
    list_labels()
