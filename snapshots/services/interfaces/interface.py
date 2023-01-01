from abc import ABCMeta, abstractmethod

from snapshots.database.models.models import Snap
from snapshots.models.snaps import SnapCreateModel, SnapUpdateModel


class ISnapService(metaclass=ABCMeta):
    """Interface for all snap service concretions."""

    @abstractmethod
    async def create_snap(self, snap_create: SnapCreateModel) -> Snap:
        """Service method for snap creation.

        :param snap_create: A pydantic model for request validation.

        :type snap_create: SnapCreateModel.

        :returns: Snap a newly created snap.

        :rtype: Snap.
        """
        ...

    @abstractmethod
    async def get_snaps(self) -> list[Snap]:
        """Service method for snap retrieval, returns all existing snaps.

        :return: list[Snap] A list of all existing snaps from the database.

        :rtype: list[Snap].
        """
        ...

    @abstractmethod
    async def get_snap(self, id: str) -> Snap:
        """Service method for snap retrieval by id.

        :param id: A string to uniquely identify the snap.

        :raises HTTPException: a 404 exception if the requested snap does not exist.

        :return: Snap An existing snap if found.

        :rtype: Snap.
        """
        ...

    @abstractmethod
    async def update_snap(self, snap_update: SnapUpdateModel) -> None:
        """Service method for updating snap.

        :param snap_update: A pydantic model for request validation.

        :raises HTTPException: a 404 exception if the requested snap does not exist.
        """
        ...

    @abstractmethod
    async def delete_snap(self, id: str) -> None:
        """Service method for snap deletion.

        :param id: A string to uniquely identify the snap.

        :raises HTTPException: a 404 exception if the requested snap does not exist.
        """
        ...
