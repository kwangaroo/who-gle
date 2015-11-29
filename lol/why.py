import urllib2, google, bs4, re, csv

################################ WHO ###########################################

def getWords():
    """
    gets a list of stopwords from a csv for later filtering

    Arguments:
        none
    
    Returns:
        list of stopwords as strings
    """
    file = open("static/stopwords.csv", 'r')
    L = []
    for line in file:
        L+=line.split(",")
    file.close()
    return L

def isStop(name,stops):
    """
    checks whether a name contains a stopword

    Arguments:
        name: string name
        stops: list of stopwords as strings
    
    Returns:
        boolean does name have a stopword
    """
    for word in name.lower().split(" "):
        if word in stops:
            return True
    return False
    
def getURLs(query):
    """
    gets a list of 15 URLs returned when google searches query

    Arguments:
        query: string query to search for
    
    Returns:
        list of URLs as strings
    """
    r = google.search(query,num=10,start=0,stop=15)
    L=[]
    for result in r:
        L.append(result)
    return L

def regNames(text):
    """
    uses regular expressions to return a list of names found in the text

    Arguments:
        text: string of text to be processed
    
    Returns:
        list of names from text

    >>> regNames("Mike Zamansky or is it Mr. Mike Zamansky or is it Mike Roft Zamansky or is it Mike Mike Zamansky Zamansky")
    ['Mike Zamansky', 'Mr. Mike Zamansky', 'Mike Roft Zamansky', 'Mike Mike Zamansky Zamansky']
    >>> regNames("Mr. Mike Zamansky or is it Dr. Mike Zamansky")
    ['Mr. Mike Zamansky', 'Dr. Mike Zamansky']
    >>> regNames("John J. Smith or is it JonAlf Dyrland-Weaver")
    ['John J. Smith', 'JonAlf Dyrland-Weaver']
    >>> regNames("Mr. M. Z.")
    ['Mr. M. Z.']
    >>> regNames("J. S. Bach or is it Johann Sebastian Bach")
    ['J. S. Bach', 'Johann Sebastian Bach']
    """
    #exp = "(((([A-Z][a-z]+)|M([rs]|rs)\.)|Dr\.)( [A-Z][a-z]+)+)"
    exp = "(((([A-Z][a-z]+([A-Z][a-z]+)*)(\-([A-Z][a-z]+([A-Z][a-z]+)*))*|M([rs]|rs)\.)|Dr\.|[A-Z]\.)(( [A-Z]([a-z]+([A-Z][a-z]+)*(\-[A-Z][a-z]+([A-Z][a-z]+)*)*))|( [A-Z]\.))+)"
    result = re.findall(exp, text)
    L = []
    for r in result:
        L.append(r[0])
    return L

def processURL(url):
    """
    takes a URL and returns the text of the URL using urllib2 and BeautifulSoup
    uses regex to remove some escape characters
    if the URL cannot be opened, empty string is returned

    Arguments:
        url: a URL as a string
    
    Retuens:
        string of text from url
    """
    try:
        u = urllib2.urlopen(url)
        page = u.read()
        soup = bs4.BeautifulSoup(page,"html.parser")
        raw = soup.get_text()
        text = re.sub("[\t\n]"," ",raw)
        return text
    except:
        return ""

def allNames(L):
    """
    wrapper for processURL and regnames
    takes list of urls, uses processURL to get the text from each one,
    and uses getNames on the text and returns a list of the name lists

    Arguments:
        L: list of URLs as strings
    
    Retuens:
        list of lists of names
    """
    M = []
    for url in L:
        text = processURL(url)
        M.append(regNames(text))
    return M

def countNames(M):
    """
    takes list of URLs, uses allNames to get the 2d list of names,
    and then uses this to create a dictionary of {name : # of occurences} pairs
    goes through the dictionary and takes out names that contain stopwords
    gets stopwords using getWords and checks names using isStop

    Arguments:
        M: list of URLs as strings
    
    Returns:
        dictionary of names and how many times they were found
    """
    stopwords = getWords()
    L = allNames(M)
    tally = {}
    for url in L:
        for name in url:
            if name in tally:
                tally[name]+=1
            else:
                tally[name]=1
    for name in tally.keys():
        if isStop(name,stopwords):
            tally.pop(name)
    return tally

def getNames(query):
    """
    wrapper for getURLs and countNames
    gets a dictionary of names and occurrences for a query

    Arguments:
        query: string query to search for
    
    Returns:
        dictionary of names and how many times they were found
    """
    urls = getURLs(query)
    return countNames(urls)

def getTopNames(query,amt):
    """
    gets a dictionary of names and occurrences for a query and returns
    a specified amount of the top names

    Arguments:
        query: string query to search for
        amt: int number of top names to return
    
    Returns:
        dictionary of names and how many times they were found
    """
    d = getNames(query)
    sorts = sorted(d.iteritems(),key=lambda(k,v):(-v,k))[:amt]
    with open('results.csv', 'wb') as csvfile:
	  spamwriter = csv.writer(csvfile)
	  for r in sorts:
	    #content = r.text.encode('utf-8').strip() + "<br><br>"
	    spamwriter.writerow((r))
    return sorts

#print getTopNames("who played spiderman",10)
#print getTopNames("who is ruining america",10)

################################ WHEN ###########################################

def getDates(text):
    """INEFFECTIVE CODE A PALOOZA :D 
    Given url text, returns list of dates that appear in it.
    Also, should ignore invalid dates."""

    dateList = []
    
#Searching for dates of MM/DD/YYYY format and compiling. This includes M/D/YYYY.
    DMYexp = "(0?[1-9]|1[012])[\/.-](0?[1-9]|[12][0-9]|3[01])[\/.-]\d{4}"
    DMYDates = re.findall(DMYexp,text)
    DMY = []
    for r in DMYDates:
        DMY.append(r)
    dateList.append(DMY)

#Searching for dates of MM/YYYY or MMM/YYYY or Month, YYYY format. 
    MYexp = "(0?[1-9]|1[012]|January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\/.-]\s?\d{4}"
    MYdates = re.findall(MYexp,text)
    MY = []
    for r in MYdates:
        MY.append(r)
    dateList.append(MY) 

#Searching for dates of MMM DD, YYYY format. 
    MDYexp = "(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec).?\s(0?[1-9]|[12][0-9]|3[01]),?\s\d{4}"
    MDYdates = re.findall(MDYexp,text)
    MDY=[]
    for r in MDYdates:
        MDY.append(r)
    dateList.append(MDY)

    return dateList 



def convertDates(dateList):
    """ Converts a date to the same format: mm/dd/yyyy 
    Returns modified date.
    KATHY, DON'T FORGET TO USE re.match"""
    return date

def countDates(urls):
    """ Returns a dictionary with the date mentioned and the number of times it pops up."""
    ct = {}
    for url in urls:
        text = processURL(url)
        dateList = getDates(text)
        for date in dateList:
            if date in tally:
                ct[name]+=1
            else:
                ct[name]=1
    return ct 

def getDateAns(query, amt):
    urls = getURLs(query)
    dateList = countDates(urls)
    #tf is ordering lol
    sorts = sorted(dateList.iteritems(),key=lambda(k,v):(-v,k))[:amt]
    return sorts

#print getDateAns("when was the war of 1812",15) 


"""to accomodate for: 
   mm-dd-yy 
   yyyy-mm-dd
 
THIS REGEX IS GONNA BE TERRIBS

Invalid Dates I May Or May Not Have To Care About: 
Feb 29th for non-leap years (
31st of feb, apr, jun, sept, nov 
"""

if __name__=="__main__":
    import doctest
    doctest.testmod()   
