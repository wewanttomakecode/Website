from peewee import PostgresqlDatabase, Model, CharField
DATABASE = 'database'
db = PostgresqlDatabase(DATABASE)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()
	message = CharField()