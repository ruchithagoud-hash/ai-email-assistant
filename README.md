# ai-email-assistant

## Overview
I often found it difficult to handle and check all my emails regularly because of the large number of daily messages. Important emails were getting mixed with promotional, spam, and less important mails, making inbox management time-consuming and inefficient.

To solve this real-life problem, I developed the Gmail Email Assistant — a Python-based automation system that helps organize emails automatically. The assistant reads unread emails, classifies them into categories, applies Gmail labels, and sends reminder summaries for important emails.

This project was built to reduce manual effort, improve productivity, and ensure that important emails are not missed even when daily email checking is not possible.
## Features

### Gmail Authentication
- Secure Gmail login using Google OAuth2 authentication
- Token-based access management

### Automatic Email Reading
- Fetches unread emails directly from Gmail inbox
- Extracts sender, subject, and email snippet

### Email Classification
Classifies emails into multiple categories:
- Important-Urgent
- Important-General
- Works
- Personals
- Spam
- Others
### Automatic Labeling
- Applies Gmail labels automatically based on classification
- Organizes inbox efficiently
### Reminder System
- Generates daily summaries of important emails
- Sends reminder emails automatically
## Technologies Used
- Python
- Gmail API
- Google OAuth2
- REST APIs
## Project Structure
```text
gmail-email-assistant/
│
├── auth.py
├── classify.py
├── config.py
├── gmail_reader.py
├── get_labels.py
├── main.py
├── reminder.py
├── .gitignore
└── README.md

File Description
auth.py
Handles Gmail authentication and generates access tokens using OAuth2.
gmail_reader.py
Reads unread emails from Gmail inbox using Gmail API.
classify.py
Contains the logic for classifying emails into different categories.
main.py
Main execution file that connects all modules and automates the workflow.
reminder.py
Creates and sends reminder summaries for important emails.
get_labels.py
Fetches Gmail labels and their IDs from the connected Gmail account.
config.py
Loads environment variables and API configurations.

How It Works
User authenticates Gmail account
System accesses unread emails
Email content is analyzed
Emails are classified into categories
Gmail labels are applied automatically
Important email summaries are generated
Reminder email is sent to the user
Setup Instructions
Step 1: Clone Repository
git clone https://github.com/your-username/gmail-email-assistant.git
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Add Gmail API Credentials
Download credentials.json from Google Cloud Console and place it inside the project folder.
Step 4: Run Authentication
python auth.py
Step 5: Execute Main Program
python main.py
Security Note
Sensitive files are excluded using .gitignore:
token.json
credentials.json
.env
pycache/
Future Enhancements
Machine Learning based email classification
Streamlit web dashboard
AI-generated email replies
Voice assistant integration
Priority scoring system
Applications
Personal email management
Productivity automation
Smart inbox organization
Important email tracking
Author

Ruchitha Arelli
