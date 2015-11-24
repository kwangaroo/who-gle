import urllib2, google, bs4, re

def getURLs(query):
    '''
    gets a list of 10 urls returned when google searches query
    '''
    r = google.search(query,num=10,start=0,stop=10)
    l=[]
    for result in r:
        l.append(result)
    return l

def regNames(text):
    '''
    uses regular expressions to return a list of names found in the text
    '''
    exp = "((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)"
    result = re.findall(exp, text)
    L = []
    for r in result:
        L.append(r[0])
    return L

def processURL(url):
    '''
    takes a url and returns the text of the url 
    '''
    #bs4 stuff

def allNames(L):
    '''
    takes list of urls, uses process url to get the text from each one,
    and uses getNames on the text and returns a list of name lists
    '''
    M = []
    for url in L:
        text = processURL(url)
        M.append(regNames(text))
    return M

def countNames(M):
    '''
    takes list of urls, uses all names to get the 2d list of names,
    and then uses this to create a dictionary of {name : # of occurences} pairs
    '''
    L = allNames(M)
    tally = {}
    for url in L:
        for name in url:
            if name in tally:
                tally[name]+=1
            else:
                tally[name]=1
    return tally

def getNames(query):
    '''
    gets a dictionary of names and occurrences for a query
    '''
    urls = getURLs(query)
    return countNames(urls)

'''
TODO
- hyphenated names
- de/von/van/etc (?)
- JonAlf
- Dr.
- Initials
- csv of names (?)
'''

print regNames("Mike Zamansky or is it Mr. Mike Zamansky or is it Mr. Dyrland-Weaver or is it Mike Roft Zamansky or is it Mike Mike Zamansky Zamansky")


### WHEN

def getDates(text):
    """HEY KATHY, DONT BE A DUNCE AND FIX THE REGEX EXPRESSION AND STICK IT WITH SOME IFS AND RUN CONVERT DATE OKAY
    Given url text, returns list of dates that appear in it.
    Also, should ignore invalid dates."""
    exp = "(0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])[\/\-]\d{4}"
    #validates for mm-dd-yyyy format as of now
    allDates = re.findall(exp,text)
        L = []
    for r in result:
        L.append(r[0])
    return L

def convertDates(L):
    """ Converts a date to the same format: mm/dd/yyyy 
    Returns modified list."""
    return L 

def countDates(urls):
    """ Returns a dictionary with the date mentioned and the number of times it pops up."""
    ct = {}
    return ct 


"""to accomodate for: 
   mm-dd-yyyy
   mm-dd-yy
   yyyy-mm-dd
   ^^those with / instead of -
   Month Day, Year 
   Perhaps MMM DD, YYYY (Apr 20, 2016) 
 
THIS REGEX IS GONNA BE TERRIBS

Invalid Dates I May Or May Not Have To Care About: 
Feb 29th for non-leap years (
31st of feb, apr, jun, sept, nov 
"""
   
