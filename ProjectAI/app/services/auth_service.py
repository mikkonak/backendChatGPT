from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.models import User
from app.dependencies import get_db

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db_session, username: str):
    return db_session.query(User).filter(User.username == username).first()


def authenticate_user(db_session, username: str, password: str):
    user = get_user(db_session, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_user(db_session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, password=hashed_password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
