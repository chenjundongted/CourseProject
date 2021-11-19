# Import Libraries
import urllib.request
from bs4 import BeautifulSoup as bs

# Removing sub-category URLs
def rmSubCatURL(urlDoc):
    lst = [x for x in urlDoc if any(c.isdigit() for c in x)]
    return lst

# Concatenate full news URLs
def concatenateFullURLs(urlDoc):
    lst = [baseUrl + x for x in urlDoc]
    return lst

# Retrieve all news URLs
baseUrl = "https://www.bbc.com"
page = urllib.request.urlopen(baseUrl+"/news")
soup = bs(page, "html.parser")
rs = soup.find("div", {"id": "news-top-stories-container"})
results = rs.find("div", {"class": "gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international"})
urlDoc = []
for link in results.find_all("a", href = True):
    newsUrl = link["href"]
    if newsUrl not in urlDoc:
        urlDoc.append(newsUrl)
urlDoc = concatenateFullURLs(rmSubCatURL(urlDoc))

# Retrieve news articles in each URL
articleDict = {}
for url in urlDoc:
    article = urllib.request.urlopen(url)
    sp = bs(article, "html.parser")
    container = sp.find("div", {"class": "ssrcss-rgov1k-MainColumn e1sbfw0p0"})
    if container is None:
        continue
    title = container.find(id = "main-heading").text.strip()
    contentContainer = container.find_all("div", {"class": "ssrcss-18snukc-RichTextContainer e5tfeyi1"})
    sentencelst = []
    for sentence in contentContainer:
        sentencelst.append(sentence.text.strip())
        content = " ".join(sentencelst)
    articleDict[title] = (content, url)

with open("bbc#1118.txt", "w") as file:
    for key, value in articleDict.items():
        file.write(key + ". " + value[0] + "\n")

with open("bbc#1118urls.text", "w") as urlFile:
    for key, value in articleDict.items():
        urlFile.write(key + ". " + value[1] + "\n")
