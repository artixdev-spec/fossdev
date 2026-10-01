from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: float


PRODUCTS: dict[int, Product] = {
    1: Product(1, "Coffee", 150.0),
    2: Product(2, "Croissant", 90.0),
    3: Product(3, "Tea", 100.0),
}


def list_products() -> list[Product]:
    return list(PRODUCTS.values())


def get_product(product_id: int) -> Product | None:
    return PRODUCTS.get(product_id)
