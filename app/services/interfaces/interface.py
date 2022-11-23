from abc import ABCMeta, abstractmethod

from app.database.models.models import Snap
from app.models.snaps import SnapCreate, SnapUpdate


class ISnapService(metaclass=ABCMeta):
    """Interface for all snap service concretions."""

    @abstractmethod
    async def create_snap(self, snap_create: SnapCreate) -> Snap:
        """Service method for snap creation.

        :param snap_create: A pydantic model for request validation.

        :type snap_create: SnapCreate.

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
    async def get_snap(self, snap_id: str) -> Snap:
        """Service method for snap retrieval by id.

        :param snap_id: A string to uniquely identify the snap.

        :raises HTTPException: a 404 exception if the requested snap does not exist.

        :return: Snap An existing snap if found.

        :rtype: Snap.
        """
        ...

    @abstractmethod
    async def update_snap(self, snap_update: SnapUpdate) -> None:
        """Service method for updating snap.

        :param snap_update: A pydantic model for request validation.

        :raises HTTPException: a 404 exception if the requested snap does not exist.
        """
        ...

    @abstractmethod
    async def delete_snap(self, snap_id: str) -> None:
        """Service method for snap deletion.

        :param snap_id: A string to uniquely identify the snap.

        :raises HTTPException: a 404 exception if the requested snap does not exist.
        """
        ...
