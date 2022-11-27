from abc import ABCMeta, abstractmethod

from snapshots.database.models.models import Snap
from snapshots.models.snaps import SnapResponseModel, SnapUpdate


class ISnapManager(metaclass=ABCMeta):
    """SnapManager interface"""

    @abstractmethod
    async def create(self, snap_data: SnapResponseModel) -> Snap:
        """Stores snapshot details in the database.

        :param snap_data: The snapshot data to be stored.

        :return: A newly created snap.

        :rtype: Snap.
        """
        ...

    @abstractmethod
    async def fetchone(self, snap_id: str) -> Snap:
        """Retrieves a snapshot from the databases using it's snap id.

        :param snap_id: A string representing a snap's id.

        :raises HTTPException: A 404 error if requested snapshot does not exist

        :return: An existing snap instance from the database.

        :rtype: Snap.
        """
        ...

    @abstractmethod
    async def fetchall(self) -> list[Snap]:
        """Retrieves all snap shots from the database.

        :return: All existing snaps from the database.

        :rtype: list[Snap].
        """
        ...

    @abstractmethod
    async def update(self, snap_update: SnapUpdate) -> None:
        """Updates a snap shot in the database.

        :param snap_update: A json with a body mapping to the snap_update.

        :raises HTTPException: A 404 error if requested snapshot does not exist.
        """
        ...

    @abstractmethod
    async def delete(self, snap: Snap) -> None:
        """Deletes a snap shot from the database using it's snap id.

        :param snap: An existing snap to be deleted from the database.

        :raises HTTPException: A 404 error if requested snapshot does not exist.
        """
        ...
