from flask import Flask, render_template, request
import requests
import smtplib

my_email = 'gabrielvictor933@gmail.com'
password = 'mwju pisc ujxj zkmy'

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/b3bcaacd5d4174d62329')
    response.raise_for_status()
    data = response.json()

    return render_template("index.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    message_sended = False
    if request.method == "POST":
        message_sended = True

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            name = request.form['name']
            email = request.form['email']
            telephone = request.form['phone']
            message = request.form['message']
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:forms submittion;\n{name}\n{email}\n{telephone}\n{message}")


    return render_template("contact.html",message_sended=message_sended)

@app.route('/post/<int:id>')
def post(id):
    response = requests.get('https://api.npoint.io/b3bcaacd5d4174d62329')
    response.raise_for_status()
    data = response.json()

    for post in data:
        if post['id'] == id:
            selected_post = post

    print(selected_post['image_url'])
    return render_template("post.html", 
                           title=selected_post['title'], 
                           subtitle=selected_post['subtitle'], 
                           body=selected_post['body'],
                           image_url=selected_post['image_url']
                           )

if __name__ == "__main__":
    app.run(debug=True)
