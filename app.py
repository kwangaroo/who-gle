from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	if request.method == "POST":
		why.getTopNames(request.form['searchterm'],20)
		f = open('results.csv','r')
		results = f.read()
		f.close()
		results = results.decode('utf-8')
		return render_template("home.html",results=sorts)
	return render_template("home.html",results='No Search Has Been Done')   

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()