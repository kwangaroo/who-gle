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
