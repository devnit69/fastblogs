from fastapi import APIRouter, Depends, Request
# from src.db.models.User import User
# from src.db.models.Blog import Blog
from src.db.models.models import User, Blog
from src.db.database import SessionLocal
from sqlalchemy.orm import Session
from src.schemas.UserCreate import UserCreate
from src.schemas.UserLogin import UserLogin
from src.schemas.UserOutput import UserOutput
from src.schemas.BlogCreate import BlogCreate
from src.utils.security import hash_password, compare_passwords
import jwt

router = APIRouter(prefix="/blogs", tags=["Blogs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_blog(request:Request, db: Session = Depends(get_db)):
    id = request.query_params.get('id')
    if id is not None:
        blog = db.query(Blog).filter(Blog.id == id).first()
        return {"msg":"blog found", "result":{'blog':blog.content}}
    # Logic to create user with email/password
    blogs = db.query(Blog).all()
    return {"msg": "All Blogs", "result":{'blog':[blog.content for blog in blogs]}}


@router.post("/")
def post_blog(blog:BlogCreate, db: Session = Depends(get_db)):
    blog_db = Blog(**blog.model_dump())
    db.add(blog_db)
    db.commit()
    db.refresh(blog_db)
    return {"msg": "Blog added successfully"}










