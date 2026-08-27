from twilio.rest import Client
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.my_email = os.environ["MY_EMAIL"]
        self.my_password = os.environ["MY_PASSWORD"]
        self.client = Client(
            os.environ["TWILIO_SID"], os.environ["TWILIO_AUTH_TOKEN"]
        )
        self.connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            to=os.environ["TWILIO_VERIFIED_NUMBER"],
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f"whatsapp:{os.environ['TWILIO_WHATSAPP_NUMBER']}",
            body=message_body,
            to=f"whatsapp:{os.environ['TWILIO_VERIFIED_NUMBER']}",
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode(
                        "utf-8"
                    ),
                )
