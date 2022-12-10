from sqlalchemy import select
from sqlalchemy.orm import Query, load_only, selectinload

from snapshots.database.models.models import Snap, SnapItem


def fetch_snap_query(snap_uuid: str) -> Query:
    """Creates an SQLAlchemy Query for retrieving a snap and it's snap_items
    by the provided snap_uuid.

    :param snap_uuid: A string by which the snap is to be retrieved.

    :return: An SQLAlchemy select Qeuery object built from the snap_uuid.

    :rtype: Query.
    """
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
    """Creates an SQLAlchemy Query for retrieving all snaps and their
    corresponding snap_items from the database.

    :return: An SQLAlchemy select Qeuery object.

    :rtype: Query.
    """
    return select(Snap).options(
        selectinload(Snap.snap_items).options(
            load_only(SnapItem.item_id, SnapItem.quantity),
        ),
    )
