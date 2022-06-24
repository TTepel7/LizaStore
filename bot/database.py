from peewee import *

db = SqliteDatabase('new.sqlite')

class Person(Model):
    id = AutoField(unique=True)
    tele_name = CharField()
    role = CharField()
    class Meta:
        database = db
        db_table = "Persons"

db.create_tables([Person])
       

Person(tele_name = 'Admin',role = 'Admin').save()