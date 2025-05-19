import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# You can set these as environment variables for security
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME")  # Your Gmail address
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Your App Password (not your login password)

def send_email(to_email: str, subject: str, body: str):
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = to_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "html"))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)

        print(f"Email successfully sent to {to_email}")
        return True

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        return False