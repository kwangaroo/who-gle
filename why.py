import urllib2, google, bs4, re

def getURLs(query):
    r = google.search(query,num=10,start=0,stop=10)
    l=[]
    for result in r:
        l.append(result)
    return l

def getNames(text):
    exp = "((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)"
    result = re.findall(exp, text)
    L = []
    for r in result:
        L.append(r[0])
    return L

print getNames("Mike Zamansky or is it Mr. Mike Zamansky or is it Mr. Dyrland-Weaver or is it Mike Roft Zamansky or is it Mike Mike Zamansky Zamansky")

'''
TODO
- hyphenated names
- de/von/van/etc (?)
- JonAlf
- Dr.
- Mister
- Doctor
'''
