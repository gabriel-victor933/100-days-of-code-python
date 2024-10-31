import requests 
import os
from twilio.rest import Client

STOCK = "RDDT"
COMPANY_NAME = '"Reddit"'
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

STOCK_URL = 'https://www.alphavantage.co/query'

NEWS_URL = 'https://newsapi.org/v2/everything'

account_sid = os.environ.get('ACCOUNT_SID')

auth_token = os.environ.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)

stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY,
    'symbol': STOCK
}

response = requests.get(STOCK_URL,stock_parameters)

response.raise_for_status()

data = response.json()


stock_data = [value for value in data['Time Series (Daily)'].values()]

last_days_data = stock_data[0:2]

open_yesterday = float(last_days_data[0]['1. open'])
close_before = float(last_days_data[1]['4. close'])

variantion = ((open_yesterday - close_before)/close_before)*100


if abs(variantion) >= 5:

    news_parameters = {
        'q': COMPANY_NAME,
        'searchIn': 'title,description',
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 3,
        'apiKey': NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_URL,news_parameters)

    news_response.raise_for_status()

    news_data = news_response.json()

    for news in news_data['articles']:
        txt = f"""
Source: {news['source']['name']}\n
Headline: {news['title']}\n
Description: {news['description']}\n
        """ 

        message = client.messages.create(
                    from_='+14435438041',
                    to='+5515981353028',
                    body=txt
                    )

        print(news['title'], message.status)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

