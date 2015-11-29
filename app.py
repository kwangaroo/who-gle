from flask import Flask, render_template, request, session, redirect, url_for

import why

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html",results='No Search Has Been Done')   


@app.route("/result")
def result():
    search = request.form['searchterm']
    answer = why.getTopNames(search,20)
    return render_template("home.html",results=answer)	

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()