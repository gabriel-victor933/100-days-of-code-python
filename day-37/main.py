import requests
import datetime as dt 
import os

TOKEN = os.environ.get('TOKEN_PIXELA')

user_params = {
    'token': TOKEN,
    'username': 'gabrielstn1927162',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

BASE_URL = 'https://pixe.la/v1/users'

graph_config = {
    'id': 'graph1',
    'name': 'control',
    'unit': 'commit',
    'type': 'int',
    'color': 'momiji',
}

header = {
    'X-USER-TOKEN': TOKEN
}

now = dt.datetime.now()



payload = {
    'quantity': '20'
}

graph_data = requests.delete(f"{BASE_URL}/{user_params['username']}/graphs/{graph_config['id']}/{now.strftime('%Y%m%d')}" ,headers=header)

print(graph_data.text)