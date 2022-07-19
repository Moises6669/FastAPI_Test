from fastapi import APIRouter
from config.db import connection_database
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get("/")
def get_user():
    return connection_database.execute(users.select()).fetchall()

@user.post("/user")
def create_user(user: User):
    new_user = {"name": user.name,"email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    connection_database.execute(users.insert().values(new_user))
    return {f"new user: {user}"}