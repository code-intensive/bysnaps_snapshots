from cloudinary import CloudinaryImage, uploader
from cloudinary.exceptions import Error as CloudinaryConnectionError
from fastapi import HTTPException
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE

from snapshots.config.settings import settings
from snapshots.database.models.models import Snap
from snapshots.utils.parsers import public_id_from_snap_url


class CloudinaryService:
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
