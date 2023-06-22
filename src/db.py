from peewee import Model, CharField, SqliteDatabase, BooleanField, AutoField
import sys

db_test = SqliteDatabase('file:foobar_database?mode=memory&cache=shared')
db = SqliteDatabase("database.db")

class BaseTable(Model):
        if "pytest" in sys.modules:
            class Meta:
                  database = db_test
        else:
            class Meta:
                database = db

class User(BaseTable):  
    id = AutoField()
    name = CharField(null=False)
    lastname = CharField(null=False)
    email  = CharField(null=False, unique=True)
    password = CharField(null=False)
    is_logged_in = BooleanField(default=False)

def reset_db_test():
    db_test.drop_tables([User])
    db_test.create_tables([User])
    db_test.close()

if "pytest" in sys.modules:
    db_test.connect()
    reset_db_test()
    
else:
    db.connect()
    db.create_tables([User])
    db.close()
