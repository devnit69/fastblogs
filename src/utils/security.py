# from passlib.context import CryptContext
import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

def hash_password(password: str) -> str:
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def compare_passwords(password, db_password):
    userBytes = password.encode('utf-8')
    print(type(db_password))
    result = bcrypt.checkpw(userBytes, db_password.encode('utf-8'))
    return result

def generate_jwt_token(user:dict):
    signing_key = os.environ.get('JWT_SIGNING_KEY')
    token = jwt.encode(user, signing_key, algorithm='HS256')
    return token




