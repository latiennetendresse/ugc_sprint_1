from pydantic import BaseModel
from pydantic import EmailStr


class TokenResponse(BaseModel):
    sub: EmailStr
    iat: int
    nbf: int
    jti: str
    exp: int
    type: str
    fresh: bool
    refresh_jti: str
    roles: list[str]
