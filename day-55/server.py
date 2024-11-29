from flask import Flask
import random

app = Flask(__name__)


random_number = random.randint(0,9)

@app.route('/')
def main():
    global random_number
    random_number = random.randint(0,9)
    return '<h1>Guess the Number: </h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route('/<int:guested>')
def guess(guested):
    if random_number == guested:
        return '<h1>You guess correctly</h1>'
    else:
        return '<h1>You have wrong!</h1>'

if __name__ == '__main__':
    app.run(debug=True)