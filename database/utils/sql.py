from sqlalchemy.future import select
from sqlalchemy.orm import load_only, selectinload

from database.models.models import Product, Snap


def fetch_snap_query(snap_uuid):
    return (
        select(Snap)
        .options(
            selectinload(Snap.products).options(
                load_only(Product.product_id, Product.quantity)
            )
        )
        .where(Snap.id == snap_uuid)
    )


def fetch_snaps_query():
    return select(Snap).options(
        selectinload(Snap.products).options(
            load_only(Product.product_id, Product.quantity)
        )
    )
