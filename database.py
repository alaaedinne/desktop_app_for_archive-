from peewee import *
import datetime 


db = SqliteDatabase('archive.db')


class Users(Model):
    nom= CharField(null=True)
    prenom = CharField(null=False)
    matriculle = CharField(unique=True)
    date_dexp = DateField()
    casie = CharField()
    row = CharField()
    col = CharField()
   

    class Meta:
        database = db

class Info__systeme(Model):
    username = CharField()
    password = CharField()
    key = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users , Info__systeme])