# Import Libraries
import urllib.request
from bs4 import BeautifulSoup as bs
import re

# Retrieve all news URLs
baseUrl = "https://www.foxnews.com/"
page = urllib.request.urlopen(baseUrl)
soup = bs(page, "html.parser")
results = soup.find("div", {"class": "main main-primary js-river"})

# Retrieve all news URLs
urlDoc = []

## Spotlight
spotlight_rs = results.find("div", {"class": "collection collection-spotlight has-hero"})
spotlight_rs_url = spotlight_rs.find("a", href = True)["href"]
urlDoc.append(spotlight_rs_url)

## Spotlight Secondary
spotlight_sd = results.find("div", {"class": "collection collection-spotlight"}).find_all("div", {"class": "m"})
for container in spotlight_sd:
    urlContainer = container.find("a", href = True)
    urlDoc.append(urlContainer["href"])

## Others
others = results.find("div", {"class": "main main-secondary"}).find_all("div", {"class": "info"})
for container in others:
    h2_container = container.find("h2")
    url = h2_container.find("a", href = True)
    urlDoc.append(url["href"])

# Retrieve news articles in each URL
articleDict = {}
for url in urlDoc:
    article = urllib.request.urlopen(url)
    sp = bs(article, "html.parser")
    hdl_container = sp.find("div", {"class": "row full"})
    if hdl_container is None:
        continue
    headline = hdl_container.find("h1").text.strip()
    if hdl_container.find("h2") is None:
        sub_headline = ""
    else:
        sub_headline = hdl_container.find("h2").text.strip()
    title = headline + ": " + sub_headline
    content_container = sp.find("div", {"class": "article-body"})
    content = content_container.find_all("p")
    sentencelst = []
    for st_container in content:
        sentence = re.sub("(\(.*\))", "", st_container.getText()).strip()
        sentencelst.append(sentence)
    text = " ".join(sentencelst)
    articleDict[title] = (text, url)

with open("fox#1206.txt", "w") as file:
    for key, value in articleDict.items():
        file.write(key + ". " + value[0] + "\n")

with open("fox#1206urls.text", "w") as urlFile:
    for key, value in articleDict.items():
        urlFile.write(key + ". " + value[1] + "\n")
