# python-api-server
Python API Test Server (Studying)

Functions
- Implement Logical Gate (NOT, AND, OR, XOR)
  - NOT, AND, OR is implemented by Perceptron
  - XOR is implemented by PyTorch
- XOR model can save & load model file.

## Dependencies
- Fast API
- PyTorch

## How To Run
- Run below command in terminal:
```
> fastapi dev main.py
```

- You need to access to `http://localhost:8000/docs` or `http://127.0.0.1:8000/docs`.
- When you access above page, you can see the API Document page (Open API Documentation - Swagger Page)
- Fast API basically supports Open API Documentation (Swagger Page).
- You can test APIs in swagger page directly.

## API Description
- `/not`, `/and`, `/or`, `/xor`, `/xor/gate-combination` requires to call `/training/~` API first.
- `/training/~` APIs are create model and training model.
- `/training/xor` API support load of trained model what you trained before.
  - if you set the `is_new_training` parameter to `True`, API will train every time that called.
  - if you set the `is_new_training` parameter to `False`, API will load model from file what you trained before.
    - if trained model file does not exist, API will create new model and train model.
