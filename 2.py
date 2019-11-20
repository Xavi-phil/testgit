import urllib.request
from bs4 import BeautifulSoup
with urllib.request.urlopen('http://www.baidu.com') as f:
    print(f.read(300))
    soup = BeautifulSoup(f, 'html.parser')
    print(soup.title)
    print(soup.title.string)
    for a in (soup.find_all('a')):
        print (a.text, a.get('href'))