from flask import Flask, request, render_template
import urllib2, google, bs4, re

app = Flask(__name__)

# This is a tiny application and only requires an app route. We can get the
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

    Returns:
        A rendered Jinja template (index.html) with the following parameters:
            QUERY = query
            RESULT = result
    """
    print "test1"

    if "query" not in request.args:
        print "test2"

        return render_template("index.html")

    print "test3"
    
    # Run a Google search for the query
    query = request.args["query"]
    print query

    
    
    #Grab the person's name from the query
    exp = "[A-Z][a-z]+\s+[A-Z][a-z]+"
    name = re.findall(exp,query)
    #Hope, the name turns out to be normal, like John Cena
    print name
    
    gsearch_res = list(google.search(query, num=10, start=0, stop=10))
    # Get the web page and strip the tags. Note that 'wgotten' is a pun from
    # the wget command for retrieving webpages from the command line.
    wgotten = urllib2.urlopen(gsearch_res[0])
    webpage = wgotten.read()
    beautified_soup = bs4.BeautifulSoup(webpage,'html')
    wtext = soup.get_text()

    #get the first paragraph
    exp = "<p>*</p>"
    result = re.findall(exp, wtext)
    
    # Run regex parsing to get the query
        # TODO: Write the code for the regex parsing
        
    # Return the rendered Jinja template
    return render_template("index.html", QUERY=query, RESULT=result)


#@app.route("/index", methods = ["GET", "POST"])
#@app.route("/index"/<tag>)
#def index(tag=""):
#    url = """
#http://en.wikipedia.org/wiki/%s
#    """
#    if tag == "":
#        return render_template("search.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8000)
