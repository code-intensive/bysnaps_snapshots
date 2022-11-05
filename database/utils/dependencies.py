from database.config.setup import async_session
from database.managers.snap_manager import SnapManager
from modules.cloud_snaps.cloudinary import CloudinarySnapService
from modules.generators.qr_snap_generator import QRCodeSnapGenerator
from services.snaps import SnapService


async def get_snap_service() -> SnapService:
    async with async_session() as session:
        async with session.begin():
            snap_manager = SnapManager(session)
            yield SnapService(
                snap_manager, QRCodeSnapGenerator(), CloudinarySnapService()
            )
