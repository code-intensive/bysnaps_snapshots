from database.utils.dependencies import get_snap_service
from fastapi import Depends
from models.snaps import DBSnap, Snap
from services.snaps_service import SnapService


def health_check() -> None:
    return None


async def create_snap(
    snap: Snap,
    snap_service: SnapService = Depends(get_snap_service),
) -> DBSnap:
    return await snap_service.create_snap(snap)


async def get_snap(
    snap_id: str,
    snap_service: SnapService = Depends(get_snap_service),
) -> DBSnap:
    snap = await snap_service.get_snap(snap_id)
    return snap.__dict__


async def get_snaps(
    snap_service: SnapService = Depends(get_snap_service),
) -> list[DBSnap]:
    snaps = await snap_service.get_snaps()
    return [snap.__dict__ for snap in snaps]
