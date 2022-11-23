from cloudinary import CloudinaryImage, uploader
from cloudinary.exceptions import Error as CloudinaryConnectionError
from fastapi import HTTPException
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE

from app.config.settings import settings
from app.database.models.models import Snap
from app.modules.cloud_snaps.interfaces.cloud_snap_interface import ICloudSnapService
from app.utils.parsers import public_id_from_snap_url


class CloudinarySnapService(ICloudSnapService):
    """Cloudinary service for snapshot cloud storage management."""

    @staticmethod
    async def upload_snap(snap: bytes) -> CloudinaryImage:
        try:
            cloudinary_snap = uploader.upload_image(
                file=snap,
                folder=settings.CLOUD_SNAP_UPLOAD_FOLDER,
            )
        except CloudinaryConnectionError as E:
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=str(E))
        else:
            return cloudinary_snap

    @staticmethod
    async def delete_snap(snap: Snap) -> None:
        try:
            uploader.destroy(
                public_id_from_snap_url(snap.snap_url),
            )
        except CloudinaryConnectionError as E:
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=str(E))
