# Problem 74: Soft Delete

## 概要 / Overview

ソフトデリートパターンを実装してください。削除フラグを使ってデータを論理削除します。
Implement the soft delete pattern using a deletion flag for logical deletion.

## 要件 / Requirements

1. `Item` モデル: `id: int`, `name: str`, `is_deleted: bool = False` / `Item` model with soft delete flag
2. `ItemCreate` モデル: `name: str` / `ItemCreate` model
3. インメモリストア: `items = {}`, `next_id = 1` / In-memory store
4. `POST /items/` - アイテムを作成し返す / Create item and return it
5. `DELETE /items/{item_id}` - ソフトデリート (is_deleted=True に設定) し `{"message": "Item soft deleted"}` を返す / Soft delete
6. `GET /items/` - 削除されていないアイテムのみを返す / Returns only non-deleted items
7. `GET /items/deleted` - 削除されたアイテムのみを返す / Returns only deleted items

## 期待される動作 / Expected Behavior

- アイテムを削除しても物理的には削除されない / Items are not physically deleted
- `GET /items/` は `is_deleted=False` のアイテムのみ返す / Returns only items where `is_deleted=False`
- `GET /items/deleted` は `is_deleted=True` のアイテムのみ返す / Returns only items where `is_deleted=True`
