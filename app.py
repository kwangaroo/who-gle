from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	if request.method == "POST":
		why.getTopNames(request.form['searchterm'],20)
		return render_template("home.html",results=sorts)

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()