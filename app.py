from flask import Flask, render_template, request, session, redirect, url_for

import why

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html",question='No Search Has Been Done',results='No Search Has Been Done')                 

@app.route("/answer", methods = ["GET", "POST"])
def answer():
    if request.form.has_key("searchterm") and request.form["searchterm"] != "":
        question = request.form["searchterm"]
        if question[:3].lower() == "who":
            why.getTopNames(question,10)
        elif question[:4].lower() == "when":
            why.getDateAns(question,5)
        else:
            return render_template("home.html",question=question,results='Invalid question!')
        f = open('results.csv','r')
        results = f.read()
        f.close()
        results = results.decode('utf-8')
        return render_template("home.html",question=question,results=results)
    return render_template("home.html",question='No',results='No Search Has Been Done')  

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()
