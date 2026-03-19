# Problem 63: Validation Error Handler

## 概要 / Overview
Implement a validation error handler that logs errors.

## 要件 / Requirements
1. `validation_errors_log` list
2. Custom handler logging `{"path": str, "error_count": int}`
3. `Product` model: `name(min_length=1)`, `price(gt=0)`, `stock(ge=0)`
4. `POST /products/` and `GET /error-log`
