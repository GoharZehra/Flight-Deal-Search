from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ["ACCOUNT_SID"]
        self.auth_token = os.environ["AUTH_TOKEN"]
        self.TwilioNumber = os.environ["TWILIO_NUMBER"]
        self.Whatsapp_Number = os.environ["WHATSAPP_NUMBER"]
        self.email_address= os.environ["EMAIL_ADDRESS"]
        self.email_password = os.environ["EMAIL_PASSWORD"]
    def send_message(self, data):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=f"LOW PRICE FLIGHT FOUND! ONLY GBP {data.price} to fly from {data.origin_airport} to {data.destination_airport},"
                        f"with {data.stops} stops departing on {data.out_date} and returning on {data.return_date}",
            from_=self.TwilioNumber,
            to=self.Whatsapp_Number,
        )

    def send_emails(self, email_list, data):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.email_address, self.email_password)
        message_body = (f"LOW PRICE FLIGHT FOUND! ONLY GBP {data.price} to fly from {data.origin_airport} to {data.destination_airport},"
                        f"with {data.stops} stops departing on {data.out_date} and returning on {data.return_date}")
        for email in email_list:
            connection.sendmail(to_addrs=email, from_addr=self.email_address,msg=message_body)