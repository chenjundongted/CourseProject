# CS 410 Final Project
## Overview
We are working on creating a dataset containing news from CNN, BBC, FOX, NBC, VOX, the Atlantic. Our code scrapes URLs, headlines and contents of the news from these media. Each article is then manually annotated with the topics. The articles in this dataset were mainly published in November and December 2021.
## Implementation
### CNN, NBC, VOX, the Atlantic
`cnn.ipynb` in `./cnn` : scrapes news from https://www.cnn.com/

`nbc.ipynb` in `./nbc` : scrapes news from https://www.nbcnews.com/

`vox.ipynb` in `./vox` : scrapes news from https://www.vox.com/

`theAtlantic.ipynb` in `./atlantic` : scrapes news from https://www.theatlantic.com/latest/

`get_js_soup` : uses webdriver object to execute javascript code and get dynamically loaded web content

`scrape_dir_page` : gets all news URLs from the corresponding platform

`scrape_news` : gets news headline and content from the given URL

`write_url` : generates a `.txt` file containing all the news headlines and URLs

`write_content` : generates a `.txt` file containing all the news headlines and contents
### Documentation Format for bbcScript.py & bbcNews
There will be two files generated in a day for the news in "https://www.bbc.com/news".
The naming format will therefore be "[NEWS SITE]#[MONTH][DAY].txt" and "[NEWS SITE]#[MONTH][DAY]urls.txt".
For example, two files generated in 11/15 should be "bbc#1115.txt" and "bbc#1115urls.txt" according to the naming format.

Format of "bbc#1115.txt":
Each news article will be put into one single line in txt file.
The starting sentence of the line is the headline of the news, while the rest of the sentences are those in main article.

Format of "bbc#1115urls.txt":
Each news article will be put into one single line in txt file.
The starting sentence of the line is the headline of the news, while the next sentence is the url of the news.
## Usage
### Install
To run the code, the following python modules are needed: bs4, re, selenium, urllib
### To run the scraper
-   Clone the GitHub:

`git clone git@github.com:chenjundongted/CourseProject.git`
#### CNN, NBC, VOX, the Atlantic
1.  Run jupyter notebook

`jupyter notebook`

2.  Open the corresponding notebook according to the news platform you want to crawl
3. Modify the output file name `news_urls_file = ''` in `write_url` and `news_contents_file = ''` in `write_content`
4.  Run the notebook
