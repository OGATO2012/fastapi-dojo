# Problem 19: Enum Parameters / Enum パラメータ

## English

Use Python `Enum` for path parameters:
1. Create `ModelName` enum with values: `alexnet`, `resnet`, `lenet`
2. `GET /models/{model_name}` returns a message based on the model:
   - `alexnet`: `{"model_name": "alexnet", "message": "Deep Learning FTW!"}`
   - `resnet`: `{"model_name": "resnet", "message": "Have some residuals!"}`
   - `lenet`: `{"model_name": "lenet", "message": "LeCNN all the images"}`

## 日本語

パスパラメータに Python の `Enum` を使ってください:
1. `alexnet`, `resnet`, `lenet` の値を持つ `ModelName` Enum を作成する
2. `GET /models/{model_name}` でモデル名に応じたメッセージを返す

## Expected Behavior

- `GET /models/alexnet` returns `{"model_name": "alexnet", "message": "Deep Learning FTW!"}`
- `GET /models/invalid` returns 422
