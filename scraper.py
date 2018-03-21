from lxml import html
import requests


class Scraper:
  def setReqi(website):
    page = requests.get(website)
    tree = html.fromstring(page.content)

  def getInfo(tag, dataitm):
    data = tree.xpath('//' + tag '[@class=' + dataitm ']/text()')

  
