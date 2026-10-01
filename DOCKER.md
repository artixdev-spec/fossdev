# Микросервисы в Docker

| Сервис            | Порт на хосте | Что делает                                             |
|-------------------|---------------|--------------------------------------------------------|
| `product_service` | 8001          | Каталог товаров: `GET /products`, `GET /products/{id}` |
| `order_service`   | 8002          | Заказы: `POST /orders`, `GET /orders`, `GET /orders/{id}` |
| `db` (PostgreSQL) | 5432          | Хранит заказы, данные в volume `pgdata`                |

`order_service` при создании заказа спрашивает цену у `product_service` по HTTP
(`PRODUCT_SERVICE_URL`) и сохраняет заказ в PostgreSQL (`DATABASE_URL`).
Без `DATABASE_URL` заказы хранятся в памяти — удобно для локального запуска.

## Запуск

```bash
docker compose up --build
```

Проверка:

```bash
curl http://localhost:8001/products
curl -X POST http://localhost:8002/orders -H "Content-Type: application/json" -d '{"product_id": 1, "quantity": 2}'
curl http://localhost:8002/orders
```

Swagger UI: http://localhost:8001/docs и http://localhost:8002/docs

Остановить: `docker compose down` (с удалением данных БД: `docker compose down -v`).

## Тесты

```bash
cd order_service && PYTHONPATH=src ../.venv/bin/pytest tests
cd product_service && PYTHONPATH=src ../.venv/bin/pytest tests
```
