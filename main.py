from bs4 import BeautifulSoup
from urllib.request import urlopen


BaseURL = 'https://www.quotes.net/mquote/'
BaseFile = 'reffrences.html'
Space = '<br>'
Split = '<hr>'

ReffrenceLimit = 10_000
Start = 0

FileStream = open(BaseFile, 'w')

for i in range(Start,ReffrenceLimit):
    urlstream = urlopen('{0}{1}'.format(BaseURL,i))
    content = urlstream.read()
    urlstream.close()
    Soup = BeautifulSoup(content)
    if i == 0:
        Styles = Soup.find_all('link')
        FileStream.write('\n'.join(str(match) for match in Soup.find_all("link")))
    Quote = Soup.find("div",{"class":"disp-mquote-int"})
    MovieName = Soup.find("h1",{"class":"movie-title"})
    FileStream.write(str(MovieName) + Space + str(Quote) + Split)
    print(MovieName)
    print("Now at index {}".format(i))
