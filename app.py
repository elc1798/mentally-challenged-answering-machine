"""
This is it guys
"""
import urllib2, google, bs4, re

app = Flask(__name__)

"""
whatever, just a test or something
"""
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


"""
This is the search page, where you type in what you want to search
"""
@app.route("/search")
@app.route("/search/")
def search():
    return render_template("home.html")

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
