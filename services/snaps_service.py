import asyncio
from datetime import datetime

from database.managers.interfaces.snap_manager_interface import ISnapManager
from database.models.models import Snap
from models.snaps import DBSnap
from models.snaps import Snap as RawSnap
from modules.cloud_snaps.interfaces.cloud_snap_interface import ICloudSnapService
from modules.generators.interfaces.snap_generator_interface import ISnapGenerator
from utils.id_generator import generate_uuid


class SnapService:
    def __init__(
        self,
        snap_manager: ISnapManager,
        snap_generator: ISnapGenerator,
        snap_cloud_service: ICloudSnapService,
    ) -> None:

        self.snap_manager = snap_manager
        self.snap_generator = snap_generator
        self.snap_cloud_service = snap_cloud_service

    async def create_snap(self, raw_snap: RawSnap) -> Snap:
        snap_id = generate_uuid("snap")
        snap = self.snap_generator.generate_snap(snap_id)
        cloudinary_snap = await self.snap_cloud_service.upload_snap(snap)
        db_snap = DBSnap(
            id=snap_id,
            created_at=datetime.now(),
            snap_url=cloudinary_snap.url,
            **raw_snap.dict()
        )
        return await self.snap_manager.create(db_snap)

    async def get_snaps(self) -> list[Snap]:
        return await self.snap_manager.fetchall()

    async def get_snap(self, snap_id: str) -> Snap:
        return await self.snap_manager.fetchone(snap_id)

    async def delete_snap(self, snap_id: str) -> None:
        snap = await self.get_snap(snap_id)
        await asyncio.gather(
            self.snap_cloud_service.delete_snap(snap.snap_url),
            self.snap_manager.delete(snap),
        )
        return None
