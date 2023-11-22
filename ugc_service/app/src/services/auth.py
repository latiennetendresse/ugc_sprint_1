from aiohttp import ClientSession
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from src.db.auth_utils import get_auth_session

base_auth_url = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class AuthService:
    def __init__(self, session: ClientSession):
        self.session = session

    async def login(self, user_mail: str, password: str) -> JSONResponse:
        login_data = {'email': user_mail, 'password': password}
        async with self.session.post(
            '/api/v1/auth/login', json=login_data, ssl=False
        ) as resp:
            return JSONResponse(status_code=resp.status, content=await resp.json())


async def get_auth_service(
    session: ClientSession = Depends(get_auth_session),
) -> AuthService:
    return AuthService(session)
