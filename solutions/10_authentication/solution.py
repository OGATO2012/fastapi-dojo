from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

FAKE_USERS_DB = {
    "alice": {"username": "alice", "password": "secret"},
    "bob": {"username": "bob", "password": "password123"},
}
# NOTE: Passwords are stored in plaintext here for simplicity.
# In production, always hash passwords using a library like passlib/bcrypt.
# Example: from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = FAKE_USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # NOTE: Using the username as the access_token is insecure and only for demonstration.
    # In production, generate a cryptographically secure token (e.g., a JWT signed with a
    # secret key using python-jose or PyJWT) so the token cannot be forged or guessed.
    return {"access_token": user["username"], "token_type": "bearer"}


@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    user = FAKE_USERS_DB.get(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": user["username"]}
