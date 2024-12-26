from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4


app = Flask(__name__)

app.secret_key = "some secret string"

bootstrap = Bootstrap4(app)

valid_email = 'admin@email.com'

valid_password = '12345678'

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if valid_email == form.email.data and valid_password == form.password.data:
                return render_template('success.html')
            else:
                return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
