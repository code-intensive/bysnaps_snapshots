from typing import Any, Protocol

from snapshots.database.models.models import Snap


class CloudSnapProtocol(Protocol):
    """Cloudinary service protocol."""

    @staticmethod
    async def upload_snap(snap: bytes) -> Any:
        """Uploads snapshot image bytes.

        :param snap: The bytes of image to be uploaded.

        :return: Details of the newly created snapshot.

        :rtype: Any.
        """
        ...

    @staticmethod
    async def delete_snap(snap: Snap) -> None:
        """Deletes a previously uploaded snapshot.

        :param snap: An existing snapshot to be deleted.
        """
        ...
