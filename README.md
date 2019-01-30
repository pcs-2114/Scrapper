# WebScrapper
A scrapper which extracts text from links of the Times Of India articles given to it.


The text file 'linksofthearticles' contains all the links from which the scrapper collects text. 

Searching for articles on HIV in the TOI page gave me a list of links to different articles. The links were on 20 pages whose
links had a part of the link common which was my input ('linksofthesearch') to 'collect_links_from_search.py'. I used a 
scrapper to collect the links and store them into linksofthearticles. The Scrapper visits all the links and collects the text 
from the articles.
