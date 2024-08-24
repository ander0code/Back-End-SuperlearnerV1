from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append("..")
from routers import Users
from routers import Login

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5501",  
    "http://127.0.0.1:5500",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(Users.course, tags=["Users"])
app.include_router(Login.login, tags=["Login"])


