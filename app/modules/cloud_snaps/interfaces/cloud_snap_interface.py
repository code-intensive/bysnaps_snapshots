from abc import ABCMeta, abstractmethod
from typing import Any

from app.database.models.models import Snap


class ICloudSnapService(metaclass=ABCMeta):
    """Cloudinary service interface."""

    @staticmethod
    @abstractmethod
    async def upload_snap(snap: bytes) -> Any:
        """Uploads snapshot image bytes.

        :param snap: The bytes of image to be uploaded.

        :return: Details of the newly created snapshot.

        :rtype: Any.
        """
        ...

    @staticmethod
    @abstractmethod
    async def delete_snap(snap: Snap) -> None:
        """Deletes a previously uploaded snapshot.

        :param snap: An existing snapshot to be deleted.
        """
        ...
