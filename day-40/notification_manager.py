from twilio.rest import Client
import smtplib

my_email = 'gabrielvictor933@gmail.com'
password = 'mwju pisc ujxj zkmy'


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,account_sid,auth_token):
        self.client = Client(account_sid, auth_token)

    def send_sms(self,text):
        print('Sending messages')
        message = self.client.messages.create(
            from_='+14435438041',
            to='+5515981353028',
            body=text
        )

        return message.status
    
    def send_emails(self,text, to_addrs):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(from_addr=my_email,to_addrs=to_addrs,msg=f"Subject: Low Price Alert!\n{text}")