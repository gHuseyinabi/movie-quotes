from bs4 import BeautifulSoup
import requests
import threading
import queue
import psutil
BaseURL = 'https://www.quotes.net/mquote/'
BaseFile = 'reffrences.html'
UserAgent = 'hi dont mind me im downloading movie quotes to use it offline thank'
Space = '<br>'
Split = '<hr>'
ReffrenceLimit = 20_000
Start = 10_000
FileStream = open(BaseFile, 'w')

Agent = {'User-Agent':UserAgent}

QuoteDict = {"class":"disp-mquote-int"}
MovieDict = {"class":"movie-title"}
MemoryToUse = 200*1024*1024  # 200MB


que = []

def GetRequest():
    print("Woo")
    global que
    if len(que) == 0:
        return
    towrite = list((params.get("MovieName") + Space + params.get("Quote") + Split + params.get("Styles","") for params in que))
    towrite = ''.join(towrite)
    FileStream.write(towrite)
    print(f"DONE {len(que)} ROWS")
    que = []

def Look(i):
    Session = requests.Session()
    Session.headers.update(Agent)
    _ = Session.get('{0}{1}'.format(BaseURL,i))
    del Session
    QueueParameters = {}
    Soup = BeautifulSoup(_.text,"html.parser")
    del _
    if i == 0:
        QueueParameters["Styles"] = Soup.find_all('link').__str__()
    QueueParameters["Quote"] = Soup.find("div",QuoteDict).__str__()
    QueueParameters["MovieName"] = Soup.find("h1",MovieDict).__str__()
    del Soup
    que.append(QueueParameters)
    del QueueParameters

for i in range(Start,ReffrenceLimit):
    if i % 20 == 0 and i > 20:
        GetRequest()
    threading.Thread(target=Look,args=(i,)).start()
    print("QUEUE LENGTH IS:",len(que)) if len(que) != 0 else None
    print(i)
GetRequest()
