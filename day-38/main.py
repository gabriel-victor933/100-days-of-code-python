import requests 
import datetime as dt
import os 

APP_ID = os.environb['APP_ID']
API_KEY = os.environb['API_KEY']
BASE_URL = 'https://trackapi.nutritionix.com'
SHEET_URL = 'https://api.sheety.co/24573dc77c230e2a5e55256b88e428ab/myWorkouts/workouts'
SHEET_SECRET = os.environb['SHEET_SECRET']

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

sheet_header = {
    'Authorization': F'Bearer {SHEET_SECRET}',
    "Content-Type": "application/json"
}

body = {
    'query': "I ran 1 mile",
    'weight_kg': 80,
    'height_cm': 169,
    'age': 25
}

text_input = input('\nTell me wich exercises you did: ')

while text_input != 'EXIT':
    try:
        response = requests.post(url=f"{BASE_URL}/v2/natural/exercise",headers=header,data=body)

        response.raise_for_status()

        data = response.json()

        now = dt.datetime.now()

        workout_info = {
            "date": now.strftime('%d/%m/%Y'),
            "time": now.strftime('%-H:%M'),
            "exercise": data['exercises'][0]['name'],
            "duration": data['exercises'][0]['duration_min'],
            "calories": data['exercises'][0]['nf_calories'],
        }

        payload = {
            "workout": workout_info
        }

        print(data)
        post_response = requests.post(url=SHEET_URL, json=payload, headers=sheet_header)

        post_response.raise_for_status()

        print("Saved\n")

        text_input = input('\nTell me wich exercises you did: ')


    except:
        print('Error. Try Again later!\n')





