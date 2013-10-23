from peewee import *

mysql_db = MySQLDatabase('rtbd', user='root', passwd='tianlang')


class MySQLModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class Movie(MySQLModel):
	name = CharField()
	href = CharField()
	fetched = BooleanField()
	last_fetched = DateTimeField()

	class Meta:
		indexes = (
			(('href',),True),
			)


class Customer(MySQLModel):
	name = CharField()
	href = CharField()
	fetched = BooleanField()
	last_fetched = DateTimeField()

	class Meta:
		indexes = (
			(('href',),True),
			)


class Customer_Movie(MySQLModel):
	customer = ForeignKeyField(Customer)
	movie = ForeignKeyField(Movie)

	class Meta:
		indexes = (
			(('customer','movie'),True),
			)