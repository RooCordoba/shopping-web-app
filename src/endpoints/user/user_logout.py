from fastapi import APIRouter, HTTPException, status, Form
from src.utils.users_functions import get_user_by_id, userLogout
from peewee import DoesNotExist


router = APIRouter()

@router.post("/user_logout")
async def user_logout(id: int = Form(...)):
    print("aaaaaaaaaa")
    try:
        if get_user_by_id(id).is_logged_in == False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no está actualmente logeado")
        userLogout(id)
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Usuario deslogeado correctamente")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no existe")