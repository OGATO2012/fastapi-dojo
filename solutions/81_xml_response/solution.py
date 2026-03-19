from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


def _user_to_xml(user: dict) -> str:
    return (
        f"<user>"
        f"<id>{user['id']}</id>"
        f"<name>{user['name']}</name>"
        f"<email>{user['email']}</email>"
        f"</user>"
    )


@app.get("/users/")
def get_users():
    inner = "".join(_user_to_xml(u) for u in USERS)
    xml = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><users>{inner}</users>"
    return Response(content=xml, media_type="application/xml")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            xml = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>{_user_to_xml(user)}"
            return Response(content=xml, media_type="application/xml")
    raise HTTPException(status_code=404, detail="User not found")
