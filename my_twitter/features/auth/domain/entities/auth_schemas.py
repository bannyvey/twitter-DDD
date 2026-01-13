from pydantic import BaseModel, EmailStr


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: int  # user_id
    exp: int
    type: str  # "access" or "refresh"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str | None


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    nickname: str
    first_name: str
    last_name: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str
