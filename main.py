import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

#Configure Gemini API with latest version and REST
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    print("API key not found. Please add it to your .env file.")
    exit()

genai.configure(api_key=GOOGLE_API_KEY, transport='rest')

#  List and use the correct model
models = genai.list_models()
print("\nAvailable Models:")
for model in models:
    print(f"Model name: {model.name}, Description: {model.description}")

# Use the correct model name (replace with the valid name from the list)
model = genai.GenerativeModel('gemini-1.5-pro')  # Use correct name

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def generate_email_content(recipient, topic):
    print("\nGenerating email content...")

    prompt = f"""
    Generate a professional email:
    To: {recipient}
    Topic: {topic}
    
    Please create a well-structured email with a subject line and body content.
    Make it professional and concise.
    Return in format:
    SUBJECT: <subject>
    BODY: <body>
    """

    response = model.generate_content(prompt)

    # Handle API errors gracefully
    if response and hasattr(response, 'text'):
        content = response.text
    else:
        print("No response from Gemini API.")
        return "Error", "Failed to generate email content."

    # Parse the response
    lines = content.split('\n')
    subject, body = '', ''

    for line in lines:
        if line.startswith('SUBJECT:'):
            subject = line.replace('SUBJECT:', '').strip()
        elif line.startswith('BODY:'):
            body = '\n'.join(lines[lines.index(line) + 1:]).strip()

    return subject, body

def create_draft_and_confirm(recipient, subject, body):
    try:
        service = get_gmail_service()

        # Create message
        message = MIMEText(body)
        message['to'] = recipient
        message['subject'] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        draft = {'message': {'raw': raw}}

        # Create the draft
        draft = service.users().drafts().create(userId='me', body=draft).execute()

        print("\nDraft Preview:")
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print(f"Body:\n{body}")

        confirm = input("\nSend this email now? (yes/no): ")

        if confirm.lower() == 'yes':
            service.users().drafts().send(userId='me', body={'id': draft['id']}).execute()
            print(" Email sent successfully!")
        else:
            print(" Email saved in drafts. You can send it later from your Gmail account.")

    except Exception as e:
        print(f" An error occurred: {e}")

def main():
    recipient = input("Enter recipient email: ")
    topic = input("Enter the topic or purpose of the email: ")

    print("\nGenerating email content using Gemini...")
    subject, body = generate_email_content(recipient, topic)

    print("\nGenerated Email Preview:")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")

    if input("\nSave this as a draft? (yes/no): ").lower() == 'yes':
        create_draft_and_confirm(recipient, subject, body)
    else:
        print(" Email generation cancelled.")

#  Correct __main__ block
if __name__ == "__main__":
    main()
