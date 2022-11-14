from cloudinary import CloudinaryImage, uploader
from cloudinary.exceptions import Error as CloudinaryConnectionError
from config.settings import settings
from fastapi import HTTPException
from fastapi.logger import logger
from modules.cloud_snaps.interfaces.cloud_snap_interface import ICloudSnapService
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from utils.parsers import public_id_from_snap_url


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
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=str(E))
        else:
            return cloudinary_snap

    @staticmethod
    async def delete_snap(snap_url: str) -> None:
        try:
            uploader.destroy(
                public_id_from_snap_url(snap_url),
            )
        except CloudinaryConnectionError as E:
            logger.log(5, str(E), exc_info=True)
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=str(E))
        else:
            return None
