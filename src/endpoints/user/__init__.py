from fastapi import APIRouter

from . import register, user_login,user_logout

router = APIRouter()

router.include_router(register.router)
router.include_router(user_login.router)
router.include_router(user_logout.router)