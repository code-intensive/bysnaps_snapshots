from snapshots.api.services.cloudinary.cloudinary_service import CloudinaryService
from snapshots.api.services.generators.qrcode_service import QRCodeGeneratorService
from snapshots.api.services.snaps.snaps_service import SnapService
from snapshots.database.config.setup import async_session
from snapshots.database.managers.snap_manager import SnapManager


async def get_snap_service() -> SnapService:
    """Function for providing SnapService to controllers via dependency injection.

    :yields SnapService: SnapService instance.
    """
    async with async_session() as session:
        async with session.begin():
            yield SnapService(
                SnapManager(session),
                QRCodeGeneratorService(),
                CloudinaryService(),
            )
