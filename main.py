from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

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
    app.run(debug=True)