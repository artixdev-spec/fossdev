import os
from dataclasses import asdict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from order_service.clients import HttpProductClient
from order_service.memory import InMemoryOrderRepository
from order_service.service import OrderRepository, ProductNotFound, create_order

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001")
DATABASE_URL = os.getenv("DATABASE_URL")


def make_repository() -> OrderRepository:
    # без DATABASE_URL (локальный запуск без БД) заказы хранятся в памяти
    if DATABASE_URL is None:
        return InMemoryOrderRepository()
    from order_service.repository import PostgresOrderRepository

    return PostgresOrderRepository(DATABASE_URL)


app = FastAPI(title="Order service")
products = HttpProductClient(PRODUCT_SERVICE_URL)
orders = make_repository()


class OrderIn(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/orders", status_code=201)
def add_order(order_in: OrderIn) -> dict:
    try:
        order = create_order(products, orders, order_in.product_id, order_in.quantity)
    except ProductNotFound:
        raise HTTPException(status_code=404, detail="Product not found") from None
    return asdict(order)


@app.get("/orders")
def list_orders() -> list[dict]:
    return [asdict(order) for order in orders.list()]


@app.get("/orders/{order_id}")
def get_order(order_id: int) -> dict:
    order = orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return asdict(order)
