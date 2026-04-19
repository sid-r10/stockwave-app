from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# -----------------------------
# TEMP DATABASE (replace later with DynamoDB)
# -----------------------------
fake_users_db = {}


# -----------------------------
# REGISTER
# -----------------------------
@router.post("/register")
def register(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(user.password)

    fake_users_db[user.email] = {
        "email": user.email,
        "password": hashed_pw
    }

    return {"message": "User registered successfully 🚀"}


# -----------------------------
# LOGIN
# -----------------------------
@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }