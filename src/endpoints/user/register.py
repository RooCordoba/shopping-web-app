import re
from fastapi import APIRouter, HTTPException, status, Form
from ...utils.users_functions import user_exist, create_user

router = APIRouter()

@router.post("/register_user")
def register_user(name : str = Form(...), lastname: str = Form(...), email : str = Form(...) , password : str = Form(...)):
    if user_exist(email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")
    elif not("@" in email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Email")
    elif len(name) < 3 or len(name) >15:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre debe contener entre 3 y 15 caracteres")  
    elif len(lastname)< 3 or len(lastname)>20:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Apellido debe contener entre 3 y 20 caracteres")
    elif len(password) < 6:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El password debe de contener minimo 6 caracteres")
    elif not re.search("[a-z]", password) or (not re.search("[A-Z]", password)) or (not re.search("[0-9]", password)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "La contraseña debe tener minimo una mayuscula, una minuscula y un numero")
    create_user(name, lastname, email, password)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User Created")

@router.post("/mytest/")
async def mytest(numero: str = Form(...)):
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail=numero)