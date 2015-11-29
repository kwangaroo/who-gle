# who-gle
Google for who (and when)<br>

### Contributors
Katherine Gershfeld, Caitlin Stanton, Kathy Wang<br>

### Project Description
Who-gle allows you to find the answers to your most burning questions, as long as they start with "who" or "when." To find your answers, we use regular expressions and google.<br>
Stopwords csv was obtained from <a href="https://code.google.com/p/anddl/downloads/detail?name=stopwords.csv">here</a>, with several added at the end.

###How to Use
This project uses a number of libraries/modules: flask, google, BeautifulSoup4<br>
Run `pip install` on the libraries.
Create a local clone of this repository and from the local repo, run `python app.py`. From a web browser, you can access who-gle from `localhost:5000/`. Now, you can search by entering your query into the search bar and submitting.
