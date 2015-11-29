from flask import Flask, render_template, request, session, redirect, url_for

import why

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html",question='No Search Has Been Done',results='No Search Has Been Done')                 

@app.route("/answer", methods = ["GET", "POST"])
def answer():
    return render_template("home.html",question='r',results='No Search Has Been Done')  

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()