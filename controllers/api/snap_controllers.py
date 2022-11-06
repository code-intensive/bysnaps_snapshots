from database.utils.dependencies import get_snap_service
from fastapi import Depends
from models.snaps import DBSnap, Snap
from services.snaps_service import SnapService


def health_check() -> None:
    """Health check for the Snaps microservice."""
    return None


async def create_snap(
    snap: Snap,
    snap_service: SnapService = Depends(get_snap_service),
) -> DBSnap:
    """
    Creates a new Snapshot from the provided Snap.

    :param snap: A dictionary mapping with the structure of the Pydantic Snap model.
    :param snap_service: A SnapService instance to be injected for creation.
    :return: A newly created snap.
    """
    return await snap_service.create_snap(snap)


async def get_snap(
    snap_id: str,
    snap_service: SnapService = Depends(get_snap_service),
) -> DBSnap:
    """
    Retrieves a Snapshot from the database, raises a 404 if the Snap does not exist.

    :param snap_id: id of the snap to be retrieved.
    :param snap_service: A SnapService instance to be injected for snap retrieval.
    :return: An existing snap, if the snap exists.
    """
    snap = await snap_service.get_snap(snap_id)
    return snap.__dict__


async def get_snaps(
    snap_service: SnapService = Depends(get_snap_service),
) -> list[DBSnap]:
    """
    Retrieves a Snapshot from the database, raises a 404 if the Snap does not exist.

    :param snap_service: A SnapService instance to be injected for snaps retrieval.
    :return: A list of existing snaps, if snaps exist.
    """
    snaps = await snap_service.get_snaps()
    return [snap.__dict__ for snap in snaps]
