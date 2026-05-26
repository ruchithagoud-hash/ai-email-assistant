from __future__ import print_function
import os
import pickle
import google.auth.transport.requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# NEW SCOPE with modify access
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send'
]


def authenticate_gmail():
    """Authenticate user and save the token.json file."""
    creds = None
    token_path = 'token.json'
    
    # Load token if it exists
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If no (valid) credentials, start login flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the new token
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    print("✅ Gmail authentication successful! token.json updated.")
    return creds

if __name__ == '__main__':
    authenticate_gmail()
