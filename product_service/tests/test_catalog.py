from product_service.catalog import get_product, list_products


def test_list_products_is_not_empty():
    assert len(list_products()) > 0


def test_get_existing_product():
    product = get_product(1)
    assert product is not None
    assert product.name == "Coffee"
    assert product.price == 150.0


def test_get_missing_product_returns_none():
    assert get_product(999) is None
