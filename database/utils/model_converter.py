from database.models.models import Snap, SnapItem
from models.snaps import SnapInDB


async def snap_from_pydantic(orm_snap: SnapInDB) -> Snap:
    snap_data = orm_snap.dict()
    snap_items_data = snap_data.pop("snap_items")
    snap_items = [SnapItem(**snap_item) for snap_item in snap_items_data]
    return Snap(snap_items=snap_items, **snap_data)
