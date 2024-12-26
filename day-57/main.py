from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/b3bcaacd5d4174d62329')
    response.raise_for_status()
    data = response.json()

    return render_template("index.html", data=data)

@app.route('/post/<id>')
def get_post(id):
    response = requests.get('https://api.npoint.io/b3bcaacd5d4174d62329')
    response.raise_for_status()
    data = response.json()

    for post in data:
        if post['id'] == int(id):
            selected_post = post

    return render_template("post.html", title=selected_post['title'], subtitle=selected_post['subtitle'], body=selected_post['body'])

if __name__ == "__main__":
    app.run(debug=True)
