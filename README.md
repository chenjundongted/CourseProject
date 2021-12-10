# CS 410 Final Project
## Overview
We are working on creating a dataset containing news from CNN, BBC, FOX, NBC, VOX, and Atlantic. Our code scrapes URLs, headlines, and contents of the news from these media websites. Each article is then manually annotated with the topics. The articles in this dataset were mainly published in November and December 2021. The final aggregated dataset is stored as `./Annotation/dataset.zip` where the single scraping news article was stored in `./WebScrapers/` naming by its website separately.
## Implementation
All the scraper programms are in `./WebScrapers/`
### BBC, FOX, CNN, NBC, VOX, and Atlantic
`bbcScript.py` in `./WebScrapers/bbcNews` : scrapes news from https://www.bbc.com/news/

`foxNews.py` in `./WebScrapers/foxNews` : scrapes news from https://www.foxnews.com/

`cnn.ipynb` in `./WebScrapers/cnn` : scrapes news from https://www.cnn.com/

`nbc.ipynb` in `./WebScrapers/nbc` : scrapes news from https://www.nbcnews.com/

`vox.ipynb` in `./WebScrapers/vox` : scrapes news from https://www.vox.com/

`theAtlantic.ipynb` in `./WebScrapers/atlantic` : scrapes news from https://www.theatlantic.com/latest/

`get_js_soup` : uses webdriver object to execute javascript code and get dynamically loaded web content

`scrape_dir_page` : scrapes all news urls from the given media link. The function executes `get_js_soup(dir_url,driver)` to load HTML content and uses `.find` `.find_all` to get the information we need. For example, in NBC.ipynb, we use `soup.find_all('li',class_='alacarte__item')` to get list of all `<li>` of class 'alacarte__item' and `link_holder.find('a')['href']` to get each URL. To avoid getting video news pages, I filtered out the ones starting with 'https://www.nbcnews.com/video/'.

`scrape_news` : gets news headline and content from the given URL. In NBC.ipynb, we use `soup.select("h1")[0].text` to get the title and `soup.find_all(class_="article-body__content")` to get the content.

`write_url` : generates a `.txt` file containing all the news headlines and URLs

`write_content` : generates a `.txt` file containing all the news headlines and contents
#### Scraping News Format Example
There will be two files generated in a day for the news in each website.
The naming format will therefore be "[NEWS SITE]#[MONTH][DAY].txt" and "[NEWS SITE]#[MONTH][DAY]urls.txt".
For example, two files generated in 11/15 from bbcNews should be "bbc#1115.txt" and "bbc#1115urls.txt" according to the naming format.

Format of "bbc#1115.txt":
Each news article will be put into one single line in txt file.
The starting sentence of the line is the headline of the news, while the rest of the sentences are the content in main article.

Format of "bbc#1115urls.txt":
Each news article will be put into one single line in txt file.
The starting sentence of the line is the headline of the news, while the next sentence is the url of the news.

## Usage of Dataset
Our dataset is in `./Annotation/dataset.zip`. After unzipping it, there will be three files:

`headline-url.txt`: Each line starts with a title of news followed by its URL, separated by a period.

`headline-content.txt`: Each line starts with a title of news followed by its content, separated by a period.

`topic annotation.txt`: Each line contains the labeled topic of the corresponding news. Each label is seperated by a comma.
## Usage of Code
### Install
To run the code, the following python modules are needed: bs4, re, selenium, urllib
### To run the scraper
-   Clone the GitHub:

`git clone git@github.com:chenjundongted/CourseProject.git`
#### CNN, NBC, VOX, and Atlantic
1.  Run jupyter notebook

`jupyter notebook`

2.  Open the corresponding notebook according to the news platform you want to crawl
3. Modify the output file name `news_urls_file = ''` in `write_url` and `news_contents_file = ''` in `write_content`
4.  Run the notebook

#### BBC and FOX
1. open the terminal and navigate to the folder containing the script
2. run `python bbcScript.py` or `python foxNews.py`
