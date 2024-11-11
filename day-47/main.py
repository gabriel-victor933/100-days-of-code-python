from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ['EMAIL_ADRESS']
password = os.environ['EMAIL_PASSWORD']

TARGET_PRICE = 100.00

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", 
}

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
response = requests.get(url, headers=header)

response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

item = soup.find(class_='aok-offscreen')
price = float(item.text.replace("$",""))

if price < TARGET_PRICE:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Product Alert!!\nproduto com desconto!")

    