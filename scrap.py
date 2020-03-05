import bs4 as bs
import urllib.request

source =urllib.request.urlopen('http://books.toscrape.com/').read()
soup = bs.BeautifulSoup(source,'lxml')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
product =soup.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a')
print(product)

