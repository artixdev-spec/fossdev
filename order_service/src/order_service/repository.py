import psycopg

from order_service.service import Order

SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total NUMERIC(12, 2) NOT NULL
)
"""

COLUMNS = "id, product_id, quantity, total"


def _to_order(row: tuple) -> Order:
    order_id, product_id, quantity, total = row
    return Order(order_id, product_id, quantity, float(total))


class PostgresOrderRepository:
    """Хранение заказов в PostgreSQL. Таблица создаётся при первом подключении."""

    def __init__(self, dsn: str) -> None:
        self._dsn = dsn
        with self._connect() as conn:
            conn.execute(SCHEMA)

    def _connect(self) -> psycopg.Connection:
        # контекстный менеджер соединения делает commit при успешном выходе
        return psycopg.connect(self._dsn)

    def add(self, product_id: int, quantity: int, total: float) -> Order:
        with self._connect() as conn:
            row = conn.execute(
                f"INSERT INTO orders (product_id, quantity, total) "
                f"VALUES (%s, %s, %s) RETURNING {COLUMNS}",
                (product_id, quantity, total),
            ).fetchone()
        assert row is not None
        return _to_order(row)

    def get(self, order_id: int) -> Order | None:
        with self._connect() as conn:
            row = conn.execute(
                f"SELECT {COLUMNS} FROM orders WHERE id = %s", (order_id,)
            ).fetchone()
        return _to_order(row) if row is not None else None

    def list(self) -> list[Order]:
        with self._connect() as conn:
            rows = conn.execute(f"SELECT {COLUMNS} FROM orders ORDER BY id").fetchall()
        return [_to_order(row) for row in rows]
