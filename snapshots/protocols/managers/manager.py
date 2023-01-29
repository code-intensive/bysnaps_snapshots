from typing import Protocol

from snapshots.database.models.models import Snap
from snapshots.models.pydantic.snaps import SnapModel, SnapUpdateModel


class SnapManagerProtocol(Protocol):
    """SnapManager Protocol"""

    async def create(self, snap_data: SnapModel) -> Snap:
        """Stores snapshot details in the database.

        :param snap_data: The snapshot data to be stored.

        :return: A newly created snap.

        :rtype: Snap.
        """
        ...

    async def fetchone(self, id: str) -> Snap:
        """Retrieves a snapshot from the databases using it's snap id.

        :param id: A string representing a snap's id.

        :raises HTTPException: A 404 error if requested snapshot does not exist

        :return: An existing snap instance from the database.

        :rtype: Snap.
        """
        ...

    async def fetchall(self) -> list[Snap]:
        """Retrieves all snap shots from the database.

        :return: All existing snaps from the database.

        :rtype: list[Snap].
        """
        ...

    async def update(self, snap_update: SnapUpdateModel) -> None:
        """Updates a snap shot in the database.

        :param snap_update: A json with a body mapping to the snap_update.

        :raises HTTPException: A 404 error if requested snapshot does not exist.
        """
        ...

    async def delete(self, snap: Snap) -> None:
        """Deletes a snap shot from the database using it's snap id.

        :param snap: An existing snap to be deleted from the database.

        :raises HTTPException: A 404 error if requested snapshot does not exist.
        """
        ...
