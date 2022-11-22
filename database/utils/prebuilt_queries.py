from sqlalchemy import select
from sqlalchemy.orm import Query, load_only, selectinload

from database.models.models import Snap, SnapItem


def fetch_snap_query(snap_uuid: str) -> Query:
    return (
        select(Snap)
        .options(
            selectinload(Snap.snap_items).options(
                load_only(SnapItem.item_id, SnapItem.quantity),
            ),
        )
        .where(Snap.id == snap_uuid)
    )


def fetch_snaps_query() -> Query:
    return select(Snap).options(
        selectinload(Snap.snap_items).options(
            load_only(SnapItem.item_id, SnapItem.quantity),
        ),
    )
