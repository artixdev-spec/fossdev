from dataclasses import asdict

from fastapi import FastAPI, HTTPException

from product_service.catalog import get_product, list_products

app = FastAPI(title="Product service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/products")
def products() -> list[dict]:
    return [asdict(product) for product in list_products()]


@app.get("/products/{product_id}")
def product(product_id: int) -> dict:
    found = get_product(product_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return asdict(found)
