from flask import Flask, request, render_template
import urllib2, google, bs4, re

app = Flask(__name__)

# This is a tiny application and only requires an app route. We can get the
# query via a GET request parameter, much like how Google itself uses the get
# parameter "q" for their query. We just need to process the query if it
# exists and render the jinja template by supplying the result for the query.
@app.route("/",methods=["GET"])
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

    if "query" not in request.args:
        return render_template("index.html")

    # Get the query from the form
    query = request.args["query"]
    
    #Grab the person's name from the query
    exp = "[A-Z][a-z]+\s+[A-Z][a-z]+"
    name = re.findall(exp,query)
    
    #Hopefully, the name turns out to be normal, like John Cena

    # Run a Google search for the query
    gsearch_res = list(google.search(query, num=10, start=0, stop=10))

    # Get the web page and strip the tags. Note that 'wgotten' is a pun from
    # the wget command for retrieving webpages from the command line.
    wgotten = urllib2.urlopen(gsearch_res[0])
    webpage = wgotten.read()
    beautified_soup = bs4.BeautifulSoup(webpage,'html')
    wtext = beautified_soup.get_text()

    # Run RegEx parsing

    # Get the stuff between the paragraph tags
    paragraph = "p>([\w\s]*)</p"
    paragraph_stuff = re.findall(exp,wtext)

    print "Query: " + query
    print "Name: " + name[0]
    print len(paragraph_stuff)

    # Filter the RegEx parsing stuff into result
    result = []
    i = 0
    while i < len(paragraph_stuff):
        result.append(paragraph_stuff[i])
        i+= 1

    # Return the rendered Jinja template
    return render_template("index.html", QUERY=query, RESULT=result)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8000)
