from flask import Flask, render_template, request, redirect
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv()
EMAIL = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
my_email = os.environ.get('MY_EMAIL')

app = Flask(__name__)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = EMAIL
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        message = request.form['guest_comments']
        email = request.form['email']
        guest = request.form['name']

        if not message or not email or not guest:
            return render_template('thankyou.html', message="Please fill all the form fields to continue", header='Mmmm...')

        try:
            msg = Message('I saw your portfolio page', sender=(guest, email), recipients=[my_email])
            msg.body = f"{message} by: {email}"
            mail.send(msg)
            return render_template('thankyou.html', header='Thank you',  message="I'll be in contact with you as soon as possible :)")
        except:
            return render_template('thankyou.html', header='Something went wrong',  message="please try again")

        
        
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)