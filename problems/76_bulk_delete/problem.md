# Problem 76: Bulk Delete

## 概要 / Overview

複数のアイテムをIDで一括削除するエンドポイントを実装してください。
Implement an endpoint to bulk delete multiple items by their IDs.

## 要件 / Requirements

1. モジュールレベルの辞書 `items` を初期状態 `{1: "Item 1", 2: "Item 2", 3: "Item 3", 4: "Item 4", 5: "Item 5"}` で定義する / Define a module-level dict `items` with initial state `{1: "Item 1", 2: "Item 2", 3: "Item 3", 4: "Item 4", 5: "Item 5"}`
2. `POST /items/bulk-delete` - `{"ids": [1, 2, 3]}` を受け取り一括削除する / Accept `{"ids": [1, 2, 3]}` and bulk delete
3. レスポンスは `{"deleted": [...], "not_found": [...]}` 形式で返す / Return response in `{"deleted": [...], "not_found": [...]}` format
4. `deleted` には実際に削除されたIDを、`not_found` には存在しなかったIDを含める / `deleted` contains actually deleted IDs, `not_found` contains IDs that didn't exist

## 期待される動作 / Expected Behavior

- 存在するIDは削除され `deleted` リストに含まれる / Existing IDs are deleted and included in `deleted` list
- 存在しないIDは `not_found` リストに含まれる / Non-existent IDs are included in `not_found` list
- 混在するIDリストでも正しく処理される / Mixed ID lists are handled correctly
