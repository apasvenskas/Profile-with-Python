import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()  

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "audrius13toto@gmail.com"
    password = os.getenv("PASSWORD") 

    if not password:
        print("No password found in environment variables!")
        return

    receiver = "audrius13toto@gmail.com"
    my_context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=my_context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")
    except smtplib.SMTPResponseException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
message = "Subject: Test Email\n\nThis is a test email from Python!"
send_email(message)

