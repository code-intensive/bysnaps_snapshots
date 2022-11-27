from fastapi import Depends

from snapshots.database.models.models import Snap
from snapshots.models.snaps import SnapCreate, SnapUpdate
from snapshots.services.dependencies import get_snap_service
from snapshots.services.interfaces.interface import ISnapService


def health_check() -> None:
    """Health check for the Snaps microservice."""


async def create_snap(
    snap: SnapCreate,
    snap_service: ISnapService = Depends(get_snap_service),
) -> Snap:
    """Creates a new Snapshot from the provided SnapCreate.

    :param snap: a dictionary mapping with
    the structure of the Pydantic SnapCreate model.

    :param snap_service: a SnapService instance to be injected for creation.

    :return: a newly created snap.

    :rtype: Snap.
    """
    return await snap_service.create_snap(snap)


async def get_snap(
    snap_id: str,
    snap_service: ISnapService = Depends(get_snap_service),
) -> Snap:
    """Retrieves a snapshot from the database,

    :param snap_id: id of the snap to be retrieved.

    :param snap_service: a SnapService instance to be injected for snap retrieval.

    :raises HTTPException: a 404 if the snap does not exist.

    :return: an existing snap.

    :rtype: Snap
    """
    return await snap_service.get_snap(snap_id)


async def get_snaps(
    snap_service: ISnapService = Depends(get_snap_service),
    limit: int = 30,
    offset: int = 50,
) -> list[Snap]:
    """Retrieves Snapshots from the database.

    :param snap_service: A SnapService instance to be injected for snaps retrieval.

    :return: a list of existing snaps.

    :rtype: list[Snap].
    """
    return await snap_service.get_snaps()


async def update_snap(
    snap_update: SnapUpdate,
    snap_service: ISnapService = Depends(get_snap_service),
) -> None:
    """Updates an existing Snapshot at the database level,

    raises a 404 if the snap does not exist.

    :param snap_update: A dictionary mapping to the pydantic SnapUpdate model.

    :param snap_service: A SnapService instance to be injected to update snap.
    """
    return await snap_service.update_snap(snap_update)


async def delete_snap(
    snap_id: str,
    snap_service: ISnapService = Depends(get_snap_service),
) -> None:
    """Deletes a Snapshot from the database, raises a 404 if the snap does not exist.

    :param snap_id: id of the snap to be deleted.

    :param snap_service: A SnapService instance to be injected for snap deletion.
    """
    return await snap_service.delete_snap(snap_id)
