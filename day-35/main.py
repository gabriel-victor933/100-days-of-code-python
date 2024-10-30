import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get('API_KEY')

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')
client = Client(account_sid, auth_token)


parameters = {
    'lat': -17.14,
    'lon': -41.9,
    'cnt': 4,
    'appid': API_KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast',parameters)

response.raise_for_status()

data = response.json()

data_weather = [weather['weather'] for weather in data['list']]

will_rain = False
for weather_list in data_weather:
    for weather in weather_list:
        if weather['id'] < 700:
            will_rain = True

if will_rain:
    print('will rain')
    message = client.messages.create(
    from_='+14435438041',
    to='+5515981353028',
    body='It\'s going to rain!!'
    )

    print(message.sid)
    print(message.status)