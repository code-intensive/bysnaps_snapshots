from abc import ABCMeta, abstractmethod

from cloudinary import CloudinaryImage


class ICloudSnapService(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def upload_snap(snap: bytes) -> CloudinaryImage:
        """Uploads the snap to"""
        ...
