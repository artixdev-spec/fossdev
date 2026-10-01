import pytest

from order_service.memory import InMemoryOrderRepository
from order_service.service import ProductNotFound, create_order


class FakeProductClient:
    def __init__(self, prices: dict[int, float]) -> None:
        self._prices = prices

    def get_price(self, product_id: int) -> float | None:
        return self._prices.get(product_id)


@pytest.fixture
def products() -> FakeProductClient:
    return FakeProductClient({1: 150.0, 2: 90.5})


@pytest.fixture
def orders() -> InMemoryOrderRepository:
    return InMemoryOrderRepository()


def test_order_total_is_price_times_quantity(products, orders):
    order = create_order(products, orders, product_id=2, quantity=3)
    assert order.total == 271.5


def test_created_order_is_saved(products, orders):
    order = create_order(products, orders, product_id=1, quantity=1)
    assert orders.get(order.id) == order
    assert orders.list() == [order]


def test_unknown_product_raises(products, orders):
    with pytest.raises(ProductNotFound):
        create_order(products, orders, product_id=999, quantity=1)
    assert orders.list() == []


@pytest.mark.parametrize("quantity", [0, -1])
def test_non_positive_quantity_raises(products, orders, quantity):
    with pytest.raises(ValueError):
        create_order(products, orders, product_id=1, quantity=quantity)
