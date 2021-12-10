import re
import urllib.request
from bs4 import BeautifulSoup as bs

with open("headline-url.txt") as text:
  lines = text.readlines()

urls = []
for line in lines:
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
    urls.append(url[0])

with open("URLonly.txt", "w") as urlFile:
    for url in urls:
        urlFile.write(url + "\n")
