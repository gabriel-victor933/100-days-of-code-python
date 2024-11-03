import requests 


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, api_token):
        self.sheet_url = sheet_url
        self.header = {
            'Authorization': f'Bearer {api_token}'
        }
        pass

    def get_rows(self):
        response = requests.get(self.sheet_url,headers=self.header)

        response.raise_for_status()

        data = response.json()

        return data['prices']
    
    def edit_row(self, id, payload):

        payload = {
            "price": payload
        }

        response = requests.put(f'{self.sheet_url}/{id}',json=payload, headers=self.header)

        response.raise_for_status()

        return response.json()
    