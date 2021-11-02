# GitHub crawler

Crawler for crawling github repository information for master's degree research
<br></br>

## Crawling GitHub repositories
In this project, I crawled github repositories related autonomous vehicle for my master's degree research. I used `PyGitHub` for crawling, if you want to know more about this library, please check [here](https://pygithub.readthedocs.io/en/latest/introduction.html).

If you would like to know more about my degree research conducted using the data collected through this crawler, please check [here](https://github.com/Kiminjo/Technology-forecasting-using-GNN).
<br></br>


## Crawled features

|data        |data type|
|:---:        |:---:|
|repository name|str|
|repository ID|int|
|owner ID|int|
|owner type|str|
|repository full name | str|
|topcis|list|
|contributors|list|
|contributor counts|int|
|stargazer counts|int|
|forker counts|int|
|created date|date|
|last updated datae|date|
|readme|str|

<br></br>

## How to Run

### Preliminaries
- Specify the keywords you want to collect in `crawling_material.py`

- Specify the date range you want to collect in main of `Github_crawling.py`



### Run the code
Run `python Github_crawling.py` in terminal  

<br></br>
## Software Requirements
- python >= 3.5
- PyGithub
- pandas 
- numpy
