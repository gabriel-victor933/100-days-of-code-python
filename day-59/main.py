from flask import Flask, render_template
import requests

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

@app.route('/contact')
def contact():
    return render_template("contact.html")

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
