import requests
from datetime import datetime
import time
import smtplib

parameters = {
    'lat': -36.0000, 
    'lng':-17.0000,
    'formatted': 0,
    'tzid': 'America/Sao_Paulo'
}

my_email = 'gabrielvictor933@gmail.com'
password = 'mwju pisc ujxj zkmy'

while True:
    try:
        print('running!')
        response1 = requests.get('http://api.open-notify.org/iss-now.json')
        response1.raise_for_status()
        data1 = response1.json()

        iss_latitude = float(data1['iss_position']['latitude'])
        iss_longitude = float(data1['iss_position']['longitude'])
        print(iss_latitude,iss_longitude)

        if abs(iss_latitude - parameters['lat']) < 5 and abs(iss_longitude - parameters['lng']) < 5:
            print('getting sunset')
            response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)

            response.raise_for_status()

            data = response.json()

            sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])

            sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

            time_now = datetime.now()

            if time_now.hour >= sunset  or time_now.hour <= sunrise:
                print('sending email')
                with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                        connection.starttls()
                        connection.login(user=my_email, password=password)   
                        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Look up!") 
            
        print('finishing')
    except:
        print('erro na execução do programa!!')
    finally:
        print('start waiting')
        time.sleep(60)

