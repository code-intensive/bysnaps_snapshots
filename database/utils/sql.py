from database.models.models import Product, Snap
from sqlalchemy.future import select
from sqlalchemy.orm import Query, load_only, selectinload


def fetch_snap_query(snap_uuid: str) -> Query:
    return (
        select(Snap)
        .options(
            selectinload(Snap.products).options(
                load_only(Product.product_id, Product.quantity),
            ),
        )
        .where(Snap.id == snap_uuid)
    )


def fetch_snaps_query() -> Query:
    return select(Snap).options(
        selectinload(Snap.products).options(
            load_only(Product.product_id, Product.quantity),
        ),
    )
