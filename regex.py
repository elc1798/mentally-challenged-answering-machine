import re

def parse(query,text):
    """
    Will parse text according to query, and return a list of strings.

    Params:
        query - (String) What you're looking for
        text - (String) The text you need to look through.

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

    exp = "The Regular Expression used to search through text"
    stuff = ["will be a list of tuples later after using re.findall"]
        
    if query[0:3]=="Who" or query[0:4]=="What" or query[0:3]=="Why" or query[0:3]=="How":
        # Get the stuff between the paragraphs tags
        exp = "p>([\w\s]*)</p"

    # If the query is asking "Where"
    if query[0:5] == "Where":
        # Look for something along the lines of "United States"
        exp = "[A-Z][a-z]+\s+[A-Z][a-z]+"

    # If the query is asking "When"
    if query[0:4] == "When":
        # Look for something along the lines of "January 1, 2015"
        exp = "[A-Z][a-z]+\s\d{1,2},\s\d\d\d\d"
    
    print query
    print exp
    print text.encode('utf-8')
    stuff = re.findall(exp,text)
    print stuff

    # Filter stuff into result
    result = []
    i = 0
    while i < len(stuff):
        result.append(stuff[i])
        i+= 1

    return result
