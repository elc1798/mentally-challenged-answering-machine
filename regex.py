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

    # Get the stuff between the paragraphs tags
    paragraph_exp = "p>([\w\s]*)</p"
    paragraph_stuff = re.findall(paragraph_exp,text)

    # If the query is asking "Who"
    # if (who)
    name_exp = "[A-Z][a-z]+\s+[A-Z][a-z]+"

    # If the query is asking "What"

    # If the query is asking "Where"

    # If the query is asking "When"

    # If the query is asking "Why"

    # If the query is asking "How"
    
    result = ""
    return result
