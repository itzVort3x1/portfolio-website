from flask import Flask, render_template, request
from dotenv import load_dotenv
import smtplib, ssl
import os
load_dotenv()

app = Flask(__name__)


FROM_EMAIL = os.getenv('from_email').encode('ascii')
FROM_PASSWORD = os.getenv('from_password').encode('ascii')
TO_EMAIL = os.getenv('to_email').encode('ascii')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        message = data["message"]
        send_email(name=name, email=email, message=message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:Message From TechSketch\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls(context=context)
        connection.login(FROM_EMAIL, FROM_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=email_message)


@app.route('/personalinfo')
def personal_info():
    return render_template("personalinfo.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run()