# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from .models import User
from .schemas import LoginRequest
from .auth import create_access_token, get_current_user, get_db
from fastapi.security import OAuth2PasswordRequestForm

Base.metadata.create_all(bind=engine)

app = FastAPI()

# On redéfinit le /auth/login pour qu'il soit compatible avec OAuth2PasswordRequestForm
# (c'est une convention recommandée par FastAPI ; on peut aussi garder notre propre schéma)
@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    OAuth2PasswordRequestForm attend des champs "username" et "password".
    Donc si tu veux conserver "email" au lieu de "username",
    tu peux dans le front ou le client HTTP, envoyer "username": "monEmail"
    """
    # Dans ce cas, l'email est dans form_data.username
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Identifiants invalides")

    # Génération du token JWT
    access_token = create_access_token({"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/auth/me")
def me(current_user: User = Depends(get_current_user)):
    """
    Endpoint protégé.
    On récupère l'utilisateur actuel via la dépendance get_current_user.
    Si le token est absent ou invalide, on aura 401.
    """
    return {
        "id": current_user.id,
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "company": current_user.company
    }
