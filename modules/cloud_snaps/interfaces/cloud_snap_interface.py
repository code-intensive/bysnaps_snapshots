from abc import ABCMeta, abstractmethod

from cloudinary import CloudinaryImage


class ICloudSnapService(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def upload_snap(snap: bytes) -> CloudinaryImage:
        """Uploads the snap to"""
        ...

    @staticmethod
    @abstractmethod
    async def delete_snap(snap_url: str) -> CloudinaryImage:
        """Delete the snap to"""
        ...
