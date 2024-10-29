import smtplib
import datetime as dt
import random

my_email = "gabrielvictor933@gmail.com"
password = "mwju pisc ujxj zkmy"


now = dt.datetime.now()

if now.weekday() == 1:
    with open('day-32/quotes.txt','r') as file:
        data = file.readlines()
        choosed = random.choice(data)


    msg = f"""Subject: Motivation\n
    {choosed}
    """

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=msg)

    



    