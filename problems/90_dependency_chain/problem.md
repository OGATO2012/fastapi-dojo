# Problem 90: Chained/Nested Dependencies

## 概要 / Overview

ネストされた依存関係チェーンを実装してください。
Implement a chain of nested dependencies.

## 要件 / Requirements

1. `get_db()` - フェイクDBを返す依存関係 / Dependency returning fake DB
2. `get_current_user(db=Depends(get_db))` - DBからユーザーを取得 / Get user from DB
3. `get_admin_user(user=Depends(get_current_user))` - 管理者チェック, 非管理者は 403 / Admin check, 403 for non-admins
4. `GET /admin/dashboard` - `get_admin_user` で保護 / Protected by `get_admin_user`
5. `GET /user/profile` - `get_current_user` で保護 / Protected by `get_current_user`

## 期待される動作 / Expected Behavior

- `GET /admin/dashboard` → 200 (alice is admin) / 200 for admin user
- `GET /user/profile` → 200 with profile data / 200 with user data
- 依存関係チェーン: db → user → admin の順に解決される / Dependency chain resolves: db → user → admin
