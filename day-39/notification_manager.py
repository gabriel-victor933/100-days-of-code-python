from twilio.rest import Client

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