from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main___":
    app.debug = True
    app.secret_key = "this is a secret key"
    app.run()
