import bs4 as bs
import urllib.request


source=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
Soup=bs.BeautifulSoup(source,'lxml')
js_test=Soup.find('p',class_='jstest')

print(js_test.text)
