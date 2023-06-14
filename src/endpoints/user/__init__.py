from fastapi import APIRouter

from . import register
from . import user_login

router = APIRouter()

router.include_router(register.router)
router.include_router(user_login.router)