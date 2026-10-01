import httpx


class HttpProductClient:
    """Клиент product service по HTTP."""

    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    def get_price(self, product_id: int) -> float | None:
        response = httpx.get(
            f"{self._base_url}/products/{product_id}", timeout=self._timeout
        )
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return float(response.json()["price"])
