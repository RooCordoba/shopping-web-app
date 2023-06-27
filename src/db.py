from peewee import Model, CharField, SqliteDatabase, BooleanField, AutoField
import sys

db = SqliteDatabase("database.db")

class BaseTable(Model):
    class Meta:
           database = db

class User(BaseTable):  
    id = AutoField()
    name = CharField(null=False)
    lastname = CharField(null=False)
    email  = CharField(null=False, unique=True)
    password = CharField(null=False)
    is_logged_in = BooleanField(default=False)

if not "pytest" in sys.modules:
    db.connect()
    db.create_tables([User])
    db.close()
