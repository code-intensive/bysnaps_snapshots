from fastapi import Depends

from snapshots.api.services.snaps.snaps_service import SnapService
from snapshots.database.models.models import Snap
from snapshots.dependencies.service_dependency import get_snap_service
from snapshots.models.pydantic.snaps import SnapCreateModel, SnapUpdateModel


def health_check() -> None:
    """Health check for the Snaps microservice."""


async def create_snap(
    snap: SnapCreateModel,
    snap_service: SnapService = Depends(get_snap_service),
) -> Snap:
    """Creates a new Snapshot from the provided SnapCreateModel.

    :param snap: a dictionary mapping with
    the structure of the Pydantic SnapCreateModel.

    :param snap_service: a SnapService instance to be injected for creation.

    :return: a newly created snap.

    :rtype: Snap.
    """
    return await snap_service.create_snap(snap)


async def get_snap(
    id: str,
    snap_service: SnapService = Depends(get_snap_service),
) -> Snap:
    """Retrieves a snapshot from the database,

    :param id: id of the snap to be retrieved.

    :param snap_service: a SnapService instance to be injected for snap retrieval.

    :raises HTTPException: a 404 if the snap does not exist.

    :return: an existing snap.

    :rtype: Snap
    """
    return await snap_service.get_snap(id)


async def get_snaps(
    snap_service: SnapService = Depends(get_snap_service),
) -> list[Snap]:
    """Retrieves Snapshots from the database.

    :param snap_service: A SnapService instance to be injected for snaps retrieval.

    :return: a paginated list of all existing snaps.

    :rtype: list[Snap].
    """
    return await snap_service.get_snaps()


async def update_snap(
    id: str,
    snap_update: SnapUpdateModel,
    snap_service: SnapService = Depends(get_snap_service),
) -> None:
    """Updates an existing Snapshot at the database level,

    raises a 404 if the snap does not exist.

    :param id: id of the snap to be updated.

    :param snap_update: A dictionary mapping to the pydantic SnapUpdateModel.

    :param snap_service: A SnapService instance to be injected to update snap.
    """
    return await snap_service.update_snap(id, snap_update)


async def delete_snap(
    id: str,
    snap_service: SnapService = Depends(get_snap_service),
) -> None:
    """Deletes a Snapshot from the database, raises a 404 if the snap does not exist.

    :param id: id of the snap to be deleted.

    :param snap_service: A SnapService instance to be injected for snap deletion.
    """
    return await snap_service.delete_snap(id)
