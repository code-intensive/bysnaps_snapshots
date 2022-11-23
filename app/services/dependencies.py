from app.database.config.setup import async_session
from app.database.managers.snap_manager import SnapManager
from app.modules.cloud_snaps.cloudinary_snaps import CloudinarySnapService
from app.modules.generators.qr_snap_generator import QRCodeSnapGenerator
from app.services.snaps_service import SnapService


async def get_snap_service() -> SnapService:
    """Function for providing SnapService to controllers via dependency injection.

    :yields SnapService: SnapService instance.
    """
    async with async_session() as session:
        async with session.begin():
            yield SnapService(
                SnapManager(session),
                QRCodeSnapGenerator(),
                CloudinarySnapService(),
            )
