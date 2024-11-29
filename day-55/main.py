from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper(*args,**kargs):
        print(args,kargs)
        return f'<b>{function()}</b>'
    
    return wrapper

@app.route('/')
def hello_world():
    return "<h1>TESTE</h1>"


@app.route('/bye')
@make_bold
def bye(is_bold):
    return f'bye'


if __name__ == '__main__':
    app.run(debug=True)