
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

with open("linksofthearticles.txt","r+") as articles:
	for line in articles:
		print (line)
		try:
			html = urlopen(line)

		except HTTPError  as e:
			print (e)

		except URLError :
			print ("Server down or incorrect domain")

		else:
			soup = BeautifulSoup(html.read(),"html.parser")
			f=open('content_of_all_the_articles.txt','a+')
			f.write("-------------------------------------------------------------------\n")
			try:
				title = soup.find('arttitle').get_text()
				
			except AttributeError as error:
				pass
			else:
				f.write(title+"\n")
			try:
				date = soup.find('span',class_='time_cptn').get_text()
			except AttributeError as error:
				pass
			else:
				f.write(date+'\n')
			try:
				content = soup.find('div', class_='Normal').get_text()
			except AttributeError as error:
				pass
			else:	
				f.write(content+'\n')

			f.write("-----------------------------------------------------------------------------------\n")

			f.close()
'''
			title = soup.find('arttitle').get_text()
			if title:
				f.write(title+'\n')

			date = soup.find('span',class_='time_cptn').get_text()
			if date:
				f.write(date+'\n')

			content = soup.find('div', class_='Normal').get_text()
			if content:
				f.write(content+'\n')
			
'''

