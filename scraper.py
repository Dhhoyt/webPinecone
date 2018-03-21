from lxml import html
import requests


class Scraper:
  def getInfo(website, tag, dataitem):
    page = requests.get(website)
    tree = html.fromstring(page.content)
    data = tree.xpath('//' + tag '[@class=' + dataitem ']/text()')

  
