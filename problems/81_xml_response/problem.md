# Problem 81: XML Response

## 概要 / Overview

XML形式でレスポンスを返すエンドポイントを実装してください。
Implement endpoints that return responses in XML format.

## 要件 / Requirements

1. `GET /users/{user_id}` - ユーザーをXML形式で返す / Return user as XML
2. `GET /users/` - 全ユーザーをXML形式で返す / Return all users as XML
3. `Response(content=xml_string, media_type="application/xml")` を使用する / Use `Response(content=xml_string, media_type="application/xml")`
4. ユーザーが存在しない場合は 404 を返す / Return 404 if user not found

## 期待される動作 / Expected Behavior

- `GET /users/1` → Content-Type: application/xml のXMLレスポンス / XML response with Content-Type: application/xml
- `GET /users/` → 全ユーザーを含むXMLレスポンス / XML response containing all users
- XMLには id, name, email フィールドが含まれる / XML contains id, name, email fields
- 存在しないユーザーIDは 404 / Non-existent user ID returns 404
