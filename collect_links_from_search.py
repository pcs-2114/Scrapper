'''
This program collects all the links from the times of india search page. 
When we search for articles in the search button the websites shows different articles and the links to them are different. 
This program collects all the links into a single text document entitled 'linksofthearticles.txt' . 
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


with open("linksofthesearch.txt","r+") as search_links:
	for line in search_links:
		try:
			html = urlopen(line)

		except HTTPError  as e:
			print (e)

		except URLError :
			print ("Server down or incorrect domain")

		else:
			soup = BeautifulSoup(html.read(),"html.parser")
			list = soup.find_all('div', class_="content" )
			for link in list:
				html= link.find('a').get('href')	
				html= 'https://timesofindia.indiatimes.com/'+html
				f=open('linksofthearticles.txt','a+')
				f.write(html+'\n')
				f.close()
			


