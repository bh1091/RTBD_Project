from peewee import *
from models import Movie, Customer, Customer_Movie

database_name = 'rtbd'
database_user = 'root'
database_passwd = 'tianlang'

database = MySQLDatabase(database_name,
	user = database_user,
	passwd = database_passwd)

database.connect()

Movie.create_table()
Customer.create_table()
Customer_Movie.create_table()

print "table created"