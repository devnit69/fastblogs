from fastapi import APIRouter, Depends, Request
# from src.db.models.User import User
from src.db.models.models import User
from src.db.database import SessionLocal
from sqlalchemy.orm import Session
from src.schemas.UserCreate import UserCreate
from src.schemas.UserLogin import UserLogin
from src.schemas.UserOutput import UserOutput
from src.utils.security import hash_password, compare_passwords, generate_jwt_token
import jwt

router = APIRouter(prefix="/auth", tags=["Registration"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def register_with_email():
    # Logic to create user with email/password
    return {"msg": "User registered via email"}


@router.post("/register")
def register_with_email(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if(existing_user is not None):
        return {"msg" : "User with same email already exists"}
    hashed_pw = hash_password(user.password)
    user_dict = user.model_dump(exclude={"password"})
    # db_user = User(**user_dict, hashed_password=hashed_pw)
    db_user = User()
    db_user.email = user.email
    db_user.hashed_password = hashed_pw
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered via email"}


@router.post('/login')
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if(existing_user is None):
        return {"msg" : "Invalid creds"}
    
    if(compare_passwords(user.password, existing_user.hashed_password)):
        output = UserOutput()
        output.email = existing_user.email
        token = generate_jwt_token(output.__dict__)
        return {'msg' : 'Log in Successful', 'data':{'token':token, 'user':output.__dict__, 'id':existing_user.id}}
    
    return {'msg':'Log in failed'}
    

@router.post('/validate')
def validate(request:Request):
    try:
        auth_header = request.headers.get('authorization')
        bearer_token = auth_header.split(' ')[1]
        data = jwt.decode(bearer_token,'some_test_jwt_sign_key', algorithms='HS256' )
        print(data)
        return data
    except Exception as ex:
        return {'msg' : 'Issue in authorization'}


    














