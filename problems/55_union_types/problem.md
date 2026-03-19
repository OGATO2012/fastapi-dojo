# Problem 55: Union Types

## English
Use `Union` types in request bodies and response models.

### Requirements:
- Create `Cat(BaseModel)` with fields: `type: str = "cat"`, `name: str`, `indoor: bool`
- Create `Dog(BaseModel)` with fields: `type: str = "dog"`, `name: str`, `breed: str`
- Create `POST /animals/` accepting `Union[Cat, Dog]` and returning the animal
- Create `GET /pets/` returning a list with one `Cat` and one `Dog`

### Expected behavior:
- `POST /animals/` with cat JSON → 200 with cat data
- `POST /animals/` with dog JSON → 200 with dog data
- `GET /pets/` → 200 with list of 2 items

---

## 日本語
リクエストボディとレスポンスモデルで`Union`型を使用してください。

### 要件:
- フィールド`type: str = "cat"`, `name: str`, `indoor: bool`を持つ`Cat(BaseModel)`を作成する
- フィールド`type: str = "dog"`, `name: str`, `breed: str`を持つ`Dog(BaseModel)`を作成する
- `Union[Cat, Dog]`を受け取り動物を返す`POST /animals/`を作成する
- 1つの`Cat`と1つの`Dog`を含むリストを返す`GET /pets/`を作成する

### 期待される動作:
- 猫のJSONで`POST /animals/` → 200で猫データ
- 犬のJSONで`POST /animals/` → 200で犬データ
- `GET /pets/` → 2つのアイテムを含むリストで200
