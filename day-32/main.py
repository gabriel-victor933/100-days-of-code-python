
import pandas
import datetime as dt
import random
import smtplib

my_email = 'gabrielvictor933@gmail.com'
password = 'mwju pisc ujxj zkmy'

now = dt.datetime.now()

data = pandas.read_csv('day-32/birthdays.csv')

birthdays_dataframe = data[(data['month'] == now.month) & (data['day'] == now.day)]

birthdays = birthdays_dataframe.to_dict(orient='records')

random_letter_number = random.randint(1,3)

with open(f'day-32/letter_templates/letter_{random_letter_number}.txt','r') as file:
    text = file.read()

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        for birthday in birthdays:    
            personal_text = text.replace('[NAME]',birthday['name'])
            connection.sendmail(from_addr=my_email,to_addrs=birthday['email'],msg=f"Subject:Happy birthday\n\n{personal_text}")

        





