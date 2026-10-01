from order_service.service import Order


class InMemoryOrderRepository:
    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}

    def add(self, product_id: int, quantity: int, total: float) -> Order:
        order = Order(len(self._orders) + 1, product_id, quantity, total)
        self._orders[order.id] = order
        return order

    def get(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)

    def list(self) -> list[Order]:
        return list(self._orders.values())
