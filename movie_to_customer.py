from peewee import *
from models import Movie, Customer, Customer_Movie
import requests
from bs4 import BeautifulSoup
import time

base_url = 'http://www.rottentomatoes.com'

movie_list = Movie.select().where(Movie.fetched == False)

for movie in movie_list:
	url = base_url + movie.href + 'reviews/'
	print movie.name
	print url

	try:
		print "1"
		page = requests.get(url)
		print "2"
		bf = BeautifulSoup(page.content)
		print "3"	
		review_list = bf.find_all('div',{'class','criticinfo'})
		#print "getting " + len(review_list) + " customer info"

		for review in review_list:
			info = review.find('a')
			customer_name = info.text
			customer_href = info.get('href')			 
			print "try to save customer " + customer_name

			try:
				customer = Customer.create(
					name = customer_name,
					href = customer_href,
					fetched = False)
				customer.save()
				print "customer saved"

				customer_movie = Customer_Movie.create(
					customer = customer,
					movie = movie)
				customer_movie.save()
				print "customer_movie saved"

			except Exception, e:
				print "exception when saving customer"

		movie.fetched = True;
		movie.save()
		print "movie fetch changed"


	except Exception, e:
		print "exception when fetching web page"
		print e
		if str(e) == "HTTP Error 403: Forbidden":
			time.sleep(100)
			continue
