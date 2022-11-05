from cloudinary import CloudinaryImage, uploader
from config.settings import settings
from modules.cloud_snaps.interfaces.cloud_snap_interface import ICloudSnapService


class CloudinarySnapService(ICloudSnapService):
    @staticmethod
    async def upload_snap(snap: bytes) -> CloudinaryImage:
        cloudinary_snap = uploader.upload_image(
            file=snap,
            folder=settings.CLOUDINARY_SNAP_UPLOAD_FOLDER,
        )
        return cloudinary_snap
