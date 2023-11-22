import json
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from src.models.auth import LoginResponse
from src.services.auth import AuthService, get_auth_service

router = APIRouter()


@router.post(
    '/login',
    summary="логин пользователя",
    description="получение авторизационного токена",
    response_description="логин",
    tags=['Auth'],
    response_model=LoginResponse,
)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthService = Depends(get_auth_service),
) -> LoginResponse | Response:
    resp = await auth_service.login(form_data.username, form_data.password)
    if resp.status_code == HTTPStatus.OK:
        data = resp.body
        return LoginResponse(token=json.loads(data)['access_token'])
    return Response(status_code=HTTPStatus.UNAUTHORIZED, content='Invalid credentials')
