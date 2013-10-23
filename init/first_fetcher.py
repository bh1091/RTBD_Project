import requests
from bs4 import BeautifulSoup
from models import *

url = 'http://www.rottentomatoes.com/dvd/top-rentals/'

page = requests.get(url)
bf = BeautifulSoup(page.content)

movie_list = bf.find('table',{'class':'center'})
movies = movie_list.find_all('tr')

for index in range(1,len(movies)):
	movie = movies[index].find('a')
	movie_name = movie.text
	movie_href = movie.get('href')
	movie_db = Movie.create(
		name = movie_name,
		href = movie_href,
		fetched = False)
	movie_db.save()
	print "movie : " + movie_db.name + "saved \n" + "href : " + movie_db.href

print "done"