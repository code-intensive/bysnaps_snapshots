from fastapi import Depends

from models.snaps import SnapCreate, SnapInDB, SnapUpdate
from services.dependencies import get_snap_service
from services.interfaces.interface import ISnapService


def health_check() -> None:
    """Health check for the Snaps microservice."""


async def create_snap(
    snap: SnapCreate,
    snap_service: ISnapService = Depends(get_snap_service),
) -> SnapInDB:
    """
    Creates a new Snapshot from the provided SnapCreate.

    :param snap: A dictionary mapping with
    the structure of the Pydantic SnapCreate model.

    :param snap_service: A SnapService instance to be injected for creation.

    :return: A newly created snap.

    """
    return await snap_service.create_snap(snap)


async def get_snap(
    snap_id: str,
    snap_service: ISnapService = Depends(get_snap_service),
) -> SnapInDB:
    """
    Retrieves a Snapshot from the database,
    raises a 404 if the snap does not exist.

    :param snap_id: id of the snap to be retrieved.

    :param snap_service: A SnapService instance to be injected for snap retrieval.

    :return: An existing snap, if the snap exists.

    """
    return await snap_service.get_snap(snap_id)


async def get_snaps(
    snap_service: ISnapService = Depends(get_snap_service),
) -> list[SnapInDB]:
    """
    Retrieves Snapshots from the database.

    :param snap_service: A SnapService instance to be injected for snaps retrieval.

    :return: A list of existing snaps, if snaps exist.

    """
    return await snap_service.get_snaps()


async def update_snap(
    snap_update: SnapUpdate,
    snap_service: ISnapService = Depends(get_snap_service),
) -> None:
    """
    Updates an existing Snapshot at the database level,

    raises a 404 if the snap does not exist.

    :param snap_update: A dictionary mapping to the pydantic SnapUpdate model.

    :param snap_service: A SnapService instance to be injected to update snap.

    :return: None, no content
    """
    return await snap_service.update_snap(snap_update)


async def delete_snap(
    snap_id: str,
    snap_service: ISnapService = Depends(get_snap_service),
) -> None:
    """
    Deletes a Snapshot from the database, raises a 404 if the snap does not exist.

    :param snap_id: id of the snap to be deleted.

    :param snap_service: A SnapService instance to be injected for snap deletion.

    :return: None, no content

    """
    return await snap_service.delete_snap(snap_id)
