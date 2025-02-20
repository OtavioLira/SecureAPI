from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, Depends, status
from pony.orm import db_session
from .database import usuario

SECRET_KEY = 'secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = '30'

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordRequestForm(tokenUrl="token")

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt