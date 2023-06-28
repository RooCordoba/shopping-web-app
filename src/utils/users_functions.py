from ..db import User

def user_exist(mail):
    query = User.select().where(User.email==mail)
    if query.exists():
        return True

def create_user(name, lastname, email, password):
    myuser = User.create(name=name, lastname=lastname, email=email, password=password)
    myuser.save()

def get_user_by_email(email):
    myUser = User.get(User.email == email)
    return myUser

def user_login(email):
    user = get_user_by_email(email)
    user.is_logged_in = True
    user.save()

def userLogout(id):
    user = get_user_by_id(id)
    user.is_logged_in = False
    user.save()

def get_user_by_id(id):
    user = User.get(User.id == id)
    return user