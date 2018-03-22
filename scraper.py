from lxml import html
import requests


class Scraper:
  
  def getInfo(website, tag, dataitem):
    page = requests.get(website)
    tree = html.fromstring(page.content)
    data = tree.xpath('//' + tag '[@class=' + dataitem ']/text()')
    info = [website, tag, dataitem]
    return info
    
  def getPage():
    pagei = getInfo.info[0]
    return pagei
    
  def getTag():
    tagi = getInfo.info[1]
    return tagi
    
  def getDataIt():
   datait = getInfo.info[2]
   return datait
