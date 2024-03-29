from snapshots.database.models.models import Snap, SnapItem
from snapshots.models.pydantic.snaps import SnapModel


def snap_from_pydantic(orm_snap: SnapModel) -> Snap:
    """Converts a Pydantic input Snap to it's corresponding SQLAlchemy instance.

    :param orm_snap: A pydantic instance with all needed values to create a snap.

    :return: An SQLAlchemy snap instance built from the orm_snap.

    :rtype: Snap.
    """
    snap_data = orm_snap.dict()
    snap_items_data = snap_data.pop("snap_items")
    snap_items = [SnapItem(**snap_item) for snap_item in snap_items_data]
    return Snap(snap_items=snap_items, **snap_data)
