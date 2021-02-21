from bs4 import BeautifulSoup
import requests
import thrading
BaseURL = 'https://www.quotes.net/mquote/'
BaseFile = 'reffrences.html'
UserAgent = 'hi dont mind me im downloading movie quotes to use it offline thank'
Space = '<br>'
Split = '<hr>'
ReffrenceLimit = 10_000
Start = 0

FileStream = open(BaseFile, 'w')
Session = requests.Session()
Session.headers.update({'User-Agent':UserAgent})

QuoteDict = {"class":"disp-mquote-int"}
MovieDict = {"class":"movie-title"}

def Look(i):
    urlstream = Session.get('{0}{1}'.format(BaseURL,i))
    content = urlstream.text
    Soup = BeautifulSoup(content)
    if i == 0:
        Styles = Soup.find_all('link')
        FileStream.write('\n'.join(str(match) for match in Soup.find_all("link")))
    Quote = Soup.find("div",QuoteDict)
    MovieName = Soup.find("h1",MovieDict)
    FileStream.write(str(MovieName) + Space + str(Quote) + Split)
    print(MovieName)
    print("Now at index {}".format(i))
for i in range(Start,ReffrenceLimit):
    threading.Thread(target=Look,args=(i,)).start()

