from fastapi import APIRouter, HTTPException, status, Form
from peewee import DoesNotExist
from ...utils.users_functions import get_user_by_email, user_login, user_exist

router = APIRouter()


@router.post("/user_login")
def login(email: str = Form(...), password: str = Form(...)):
    try:
        if get_user_by_email(email).password == password:
            user_login(email)
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Usuario logeado correctamente")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no coincide con el email ingresado")
    except DoesNotExist :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email no registrado")