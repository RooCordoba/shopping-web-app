from peewee import Model, CharField, SqliteDatabase, PrimaryKeyField, BooleanField

db = SqliteDatabase('database.db')

class BaseTable(Model):
    class Meta:
        database = db

class User(BaseTable):
    id = PrimaryKeyField()
    name = CharField(null=False)
    lastname = CharField(null=False)
    email  = CharField(null=False, unique=True)
    password = CharField(null=False)
    is_logged_in = BooleanField(default=False)
