# app/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User
import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    """
    Génère un token JWT avec une date d'expiration.
    :param data: un dict contenant les infos à mettre dans le JWT (ex: {"sub": user.email})
    :return: le token JWT signé (string)
    """
    to_encode = data.copy()

    # Calculer la date d'expiration
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Générer le token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
# On indique que le token est récupéré depuis un endpoint "/auth/login",
# c’est juste pour la doc Swagger, ça n'empêche pas de le récupérer depuis un autre endpoint.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Dépendance qui va :
      - Extraire le token depuis le header 'Authorization: Bearer ...'
      - Décoder le token
      - Récupérer l'utilisateur en BDD
    """
    from .config import SECRET_KEY, ALGORITHM  # on peut importer ici ou globalement

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Jeton d'authentification invalide",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Décoder le token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # On s'attend à ce qu'il y ait un "sub" = email
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception

    # Rechercher l'utilisateur en base
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user
