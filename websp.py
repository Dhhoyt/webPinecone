from lxml import html
import requests

def showLogo():
  print("welcome to webPinecone!")
website = input("Enter a website you want to scrape")
tag = input("Enter the tag(s)")
dataitem = input ("Enter a data item")

scrinf = Scraper.getInfo(website, tag, dataitem)

print(scrinf)
