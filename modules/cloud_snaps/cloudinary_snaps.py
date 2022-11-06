from cloudinary import CloudinaryImage, uploader
from cloudinary.exceptions import Error as CloudinaryConnectionError
from config.settings import settings
from fastapi import HTTPException
from fastapi.logger import logger
from modules.cloud_snaps.interfaces.cloud_snap_interface import ICloudSnapService
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE


class CloudinarySnapService(ICloudSnapService):
    @staticmethod
    async def upload_snap(snap: bytes) -> CloudinaryImage:
        try:
            cloudinary_snap = uploader.upload_image(
                file=snap,
                folder=settings.CLOUDINARY_SNAP_UPLOAD_FOLDER,
            )
        except CloudinaryConnectionError as E:
            logger.log(3, E.__str__(), exc_info=True)
            detail = [
                {
                    "loc": [
                        "cloudinary_snaps",
                        "upload_snap",
                    ],
                    "type": "cloudinary.errors.connection_timeout",
                    "msg": "Service temporarily unavailable, please try again",
                },
            ]
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=detail) from E
        else:
            return cloudinary_snap
