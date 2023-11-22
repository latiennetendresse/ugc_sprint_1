from http import HTTPStatus

import jwt
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.responses import Response

from src.models.data import TokenResponse
from src.services.film_views import FilmViewService, film_view_services

SECRET_KEY = "secretfghjrtyui"
ALGORITHM = "HS256"

router = APIRouter()

api_key_scheme = APIKeyHeader(name="Authorization")


async def get_decode_token(
    token: str = Depends(api_key_scheme),
) -> TokenResponse | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenResponse(**payload)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post(
    "/send",
    status_code=HTTPStatus.OK,
    tags=["view_info"],
    description="отправить timestamp",
    summary="отправить timestamp",
)
async def send_timestamp(
    film_id: int,
    timestamp_id: int,
    token: TokenResponse = Depends(get_decode_token),
    service: FilmViewService = Depends(film_view_services),
) -> Response:
    await service.send_timestamp(token.sub, film_id, timestamp_id)
    return Response(status_code=HTTPStatus.OK)
