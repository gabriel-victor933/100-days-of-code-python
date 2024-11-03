import requests 


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, api_token):
        self.sheet_url = sheet_url
        self.header = {
            'Authorization': f'Bearer {api_token}'
        }
        pass

    def get_prices_rows(self):
        response = requests.get(f"{self.sheet_url}/prices",headers=self.header)

        response.raise_for_status()

        data = response.json()

        return data['prices']
    
    def edit_prices_row(self, id, payload):

        payload = {
            "price": payload
        }

        response = requests.put(f'{self.sheet_url}/prices/{id}',json=payload, headers=self.header)

        response.raise_for_status()

        return response.json()

    def get_email_list(self):
        response = requests.get(f"{self.sheet_url}/users",headers=self.header)

        response.raise_for_status()

        data = response.json()

        return [user['whatIsYourEmail?'] for user in data['users']]
    