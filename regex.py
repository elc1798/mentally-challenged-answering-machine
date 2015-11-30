import re, xml.etree.ElementTree

def parse(query,soup):
    """
    Will parse soup according to query, and return a list of strings.

    Params:
        query - (String) What you're looking for
        soup - (Beautiful Soup Object) The object you need to look through.

    Returns:
        result - (String) Information you were looking for in text.
    """

    # If the query is asking "Who", "What", "Why", "How"
       # for example, 
       # "Who is John Cena?"
       # "What is hydrogen sulfide?"
       # "Why did the US enter the Vietnam War?"
       # "How did the Union prevail over the Confederacy?"
    # it would be better to have answers that are paragraphs
    # they are more likely to answer the question

    text = soup.prettify()
    exp = "The Regular Expression used to search through text"
    stuff = ["will be a list of tuples later after using re.findall"]
        
    if query[0:3]=="Who" or query[0:4]=="What" or query[0:3]=="Why" or query[0:3]=="How":
        # Get the stuff between the paragraphs tags
        stuff = soup.findAll("p")

    # If the query is asking "Where"
       # for example
          # Where is New York?
    if query[0:5] == "Where":
        # Look for something along the lines of "United States"
        exp = "[A-Z][a-z]+\s+[A-Z][a-z]+"
        stuff = re.findall(exp,text)

    # If the query is asking "When"
       # for example
          # When did the US bomb Japan?
    if query[0:4] == "When":
        # Look for something along the lines of "January 1, 2015"
        exp = "[A-Z][a-z]+\s\d{1,2},\s\d\d\d\d"
        stuff = re.findall(exp,text)

    # Filter stuff into result
    result = []
    i = 0
    while i < len(stuff):
        # if the query was asking who/what/why/how, then get rid of html tags
        if exp == "The Regular Expression used to search through text":
            pretty_stuff = remove_tags(stuff[i])
            result.append(pretty_stuff)
        else:
            result.append(stuff[i])
        i+= 1

    return result

def remove_tags(text):
    """
    Removes HTML tags in a string.

    Params:
        text - (String) HTML Code

    Returns:
        result - (String) text without HTML tags
    """
    return ''.join(xml.etree.ElementTree.fromstring(str(text)).itertext())
