from fastapi import FastAPI
from src.routes import auth, blogs


app = FastAPI()


app.include_router(auth.router)
app.include_router(blogs.router)