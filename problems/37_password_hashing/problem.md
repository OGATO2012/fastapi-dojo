# Problem 37: Password Hashing

## Topic
Password Hashing - Hash and verify passwords with passlib

## Task
Create a FastAPI application with password hashing using passlib bcrypt:

1. `POST /hash-password` - Accept `{"password": "..."}` and return `{"hashed_password": "..."}`
2. `POST /verify-password` - Accept `{"password": "...", "hashed_password": "..."}` and return `{"is_valid": true/false}`

## タスク（日本語）
passlibのbcryptを使ってパスワードのハッシュ化と検証を行うエンドポイントを実装してください。

## Expected Behavior
- POST /hash-password returns a bcrypt hashed string
- POST /verify-password with correct password returns is_valid=True
- POST /verify-password with wrong password returns is_valid=False
