from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests
import datetime as dt
import os

SHEET_URL = os.environb['SHEET_URL']
API_TOKEN = os.environb['API_TOKEN']

API_KEY = os.environb['API_KEY']
API_SECRET = os.environb['API_SECRET']

ACCOUNT_SID = os.environb['ACCOUNT_SID']
AUTH_TOKEN = os.environb['AUTH_TOKEN']

def fill_sheet_iata_gaps(cities):
    for city in cities:
        try:
            if len(city['iataCode']) > 2:
                continue

            city_flight_data = flightSearch.get_iata_code(city['city'])

            city['iataCode'] = city_flight_data['iataCode']

            dataManager.edit_row(city['id'],city)

        except requests.exceptions.HTTPError: 
            print(f"Error at find city {city['city']}")

def create_sms_message(price,departure, arrivel,date):
    return f"""
Low price alert! Only {price} to {departure} to {arrivel}, on {date}
"""

dataManager = DataManager(SHEET_URL,API_TOKEN)

cities = dataManager.get_rows()

flightSearch = FlightSearch(API_KEY, API_SECRET, "GRU")

notificationManager = NotificationManager(ACCOUNT_SID,AUTH_TOKEN)

fill_sheet_iata_gaps(cities)

now = dt.datetime.now()
one_day = dt.timedelta(days=1)

for i in range(180): #aproximadamente 6 meses
    print(now.strftime('%Y-%m-%d'))
    for city in cities:
        try:
            flights_data = flightSearch.get_flight_offers(city['iataCode'],now.strftime('%Y-%m-%d'),city['lowestPrice'])

            if len(flights_data) > 0:

                for destination in flights_data:
                    print(city['city'],destination['price']['total'])
                    price = destination['price']['total']
                    notificationManager.send_sms(create_sms_message(price,flightSearch.origin_code ,city['iataCode'],now.strftime('%Y-%m-%d')))

            else:
                print(city['city'],"N/A")

        except requests.exceptions.HTTPError: 
                print(f"Error at find city {city['city']}")

    
    now = now + one_day

