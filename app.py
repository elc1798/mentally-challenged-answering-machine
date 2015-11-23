from flask import Flask, request, render_template
import urllib2, google, bs4, re

app = Flask(__name__)

# This is a tiny application and only requires a app route. We can get the
# query via a GET request parameter, much like how Google itself uses the get
# parameter "q" for their query. We just need to process the query if it
# exists and render the jinja template by supplying the result for the query.
@app.route("/")
def search():
    """
    Performs a search if given a query via a GET parameter (query) and returns a
    rendered Jinja template

    Params:
        none

"""
This is the results page
"""
@app.route("/results")
@app.route("/results/")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8000)
