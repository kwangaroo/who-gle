import urllib2, google, bs4, re

################################ WHO ###########################################

def getURLs(query):
    '''
    gets a list of 10 urls returned when google searches query
    '''
    r = google.search(query,num=10,start=0,stop=15)
    l=[]
    for result in r:
        l.append(result)
    return l

def regNames(text):
    '''
    uses regular expressions to return a list of names found in the text
    '''
    exp = "((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)"
    exp = "(((([A-Z][a-z]+)|M([rs]|rs)\.)|Dr\.)( [A-Z][a-z]+)+)"
    exp = "(((([A-Z][a-z]+)(\-([A-Z][a-z]+))*|M([rs]|rs)\.)|Dr\.)( ([A-Z][a-z]+)(\-([A-Z][a-z]+))*)+)"
    result = re.findall(exp, text)
    L = []
    for r in result:
        L.append(r[0])
    return L

def processURL(url):
    '''
    takes a url and returns the text of the url 
    '''
    text = ""
    try:
        u = urllib2.urlopen(url)
        page = u.read()
        soup = bs4.BeautifulSoup(page,"html.parser")
        raw = soup.get_text()
        text = re.sub("[\t\n]"," ",raw)
    except:
        ""
    return text

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

def getTopNames(query,amt):
    '''
    gets a dictionary of names and occurrences for a query and returns
    a specified amount of the top names
    '''
    d = getNames(query)
    sorts = sorted(d.iteritems(),key=lambda(k,v):(-v,k))[:amt]
    return sorts

'''
TODO
- de/von/van/etc (?)
- JonAlf
- Initials
- csv of names/words (?)
'''

print regNames("Mike Zamansky or is it Mr. Mike Zamansky or is it Mr. Dyrland-Weaver or is it Mike Roft Zamansky or is it Mike Mike Zamansky Zamansky")
print regNames("Mike Zamansky or is it Mr. Mike Zamansky or is it Dr. Mike Zamansky")
print regNames("Dyrland-Weaver Weaver-Dyrland")

print getTopNames("who created stuycs",20)


################################ WHEN ###########################################

def getDates(text):
    """INEFFECTIVE CODE A PALOOZA :D 
    Given url text, returns list of dates that appear in it.
    Also, should ignore invalid dates."""

    dateList = []
    
#Searching for dates of MM/DD/YYYY format and compiling. This includes M/D/YYYY.
#DOES NOT INCLUDE M/D/YY OR MM/DD/YY GET ON THAT KATHY
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
    return ct 


"""to accomodate for: 
   mm-dd-yy 
   yyyy-mm-dd
 
THIS REGEX IS GONNA BE TERRIBS

Invalid Dates I May Or May Not Have To Care About: 
Feb 29th for non-leap years (
31st of feb, apr, jun, sept, nov 
"""
   
