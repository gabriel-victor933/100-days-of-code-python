import requests   

BASE_URL = 'https://test.api.amadeus.com'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key, api_secret, origin_code):

        self.origin_code = origin_code

        data = {
            'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret
        }

        response = requests.post(F'{BASE_URL}/v1/security/oauth2/token', data=data,headers={"Content-Type": "application/x-www-form-urlencoded"})

        response.raise_for_status()

        data = response.json()

        self.access_token = data['access_token']

        self.header = {
            'Authorization': f'Bearer {self.access_token}'
        }

    
    def get_iata_code(self, keyword):

        params = {
            'keyword': keyword,
            'max': 1
        }

        response = requests.get(f'{BASE_URL}/v1/reference-data/locations/cities', params=params, headers=self.header)

        response.raise_for_status()

        data = response.json()

        return data['data'].pop()
    
    def get_flight_offers(self,destionation_code, departur_date, max_price, is_direct = True):

        params = {
            'originLocationCode': self.origin_code,
            'destinationLocationCode': destionation_code,
            'departureDate': departur_date,
            'adults': 1,
            'max': 10,
            'maxPrice': max_price,
            'nonStop': 'true' if is_direct else 'false',
            'currencyCode': 'GBP'
        }

        response = requests.get(f"{BASE_URL}/v2/shopping/flight-offers",headers=self.header, params=params)

        data =  response.json()
        
        if data.get('data') is None:
            return []

        return data['data']