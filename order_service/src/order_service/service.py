from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    id: int
    product_id: int
    quantity: int
    total: float


class ProductNotFound(Exception):
    pass


class ProductClient(Protocol):
    def get_price(self, product_id: int) -> float | None: ...


class OrderRepository(Protocol):
    def add(self, product_id: int, quantity: int, total: float) -> Order: ...

    def get(self, order_id: int) -> Order | None: ...

    def list(self) -> list[Order]: ...


def create_order(
    products: ProductClient,
    orders: OrderRepository,
    product_id: int,
    quantity: int,
) -> Order:
    """Создать заказ: узнать цену товара в product service и сохранить заказ."""
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    price = products.get_price(product_id)
    if price is None:
        raise ProductNotFound(product_id)
    return orders.add(product_id, quantity, round(price * quantity, 2))
