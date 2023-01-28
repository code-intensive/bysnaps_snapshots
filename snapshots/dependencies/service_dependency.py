from snapshots.database.config.setup import async_session
from snapshots.database.managers.snap_manager import SnapManager
from snapshots.services.cloudinary.cloudinary_service import CloudinaryService
from snapshots.services.generators.qrcode_service import QRCodeGeneratorService
from snapshots.services.snaps.snaps_service import SnapService


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
