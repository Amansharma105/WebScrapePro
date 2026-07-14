import smtplib

def send_email(recipient, subject, message):
    print(f"Sending email to {recipient}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
