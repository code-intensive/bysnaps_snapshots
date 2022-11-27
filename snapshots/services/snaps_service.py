import asyncio
from datetime import datetime

from snapshots.database.managers.interfaces.snap_manager_interface import ISnapManager
from snapshots.database.models.models import Snap
from snapshots.models.snaps import SnapCreate, SnapResponseModel, SnapUpdate
from snapshots.modules.cloud_snaps.interfaces.cloud_snap_interface import (
    ICloudSnapService,
)
from snapshots.modules.generators.interfaces.snap_generator_interface import (
    ISnapGenerator,
)
from snapshots.services.interfaces.interface import ISnapService
from snapshots.utils.id_generator import generate_uuid


class SnapService(ISnapService):
    """SnapService class."""

    def __init__(
        self,
        snap_manager: ISnapManager,
        snap_generator: ISnapGenerator,
        snap_cloud_service: ICloudSnapService,
    ) -> None:
        self.snap_manager = snap_manager
        self.snap_generator = snap_generator
        self.snap_cloud_service = snap_cloud_service

    async def create_snap(self, snap_create: SnapCreate) -> Snap:
        snap = await self._build_snap(snap_create)
        return await self.snap_manager.create(snap)

    async def get_snaps(self) -> list[Snap]:
        return await self.snap_manager.fetchall()

    async def get_snap(self, snap_id: str) -> Snap:
        return await self.snap_manager.fetchone(snap_id)

    async def update_snap(self, snap_update: SnapUpdate) -> None:
        return await self.snap_manager.update(snap_update)

    async def delete_snap(self, snap_id: str) -> None:
        snap = await self.get_snap(snap_id)
        await asyncio.gather(
            self.snap_cloud_service.delete_snap(snap),
            self.snap_manager.delete(snap),
        )

    async def _build_snap(self, snap_create: SnapCreate) -> SnapResponseModel:
        """Private method for snap building.

        :param snap_create: A pydantic model for request validation.

        :return: A pydantic model mapping to an SQLAlchemy Snap model.

        :rtype: SnapResponseModel.
        """
        snap_id = generate_uuid("snap")
        snap_bytes = self.snap_generator.generate_snap(snap_id)
        cloudinary_snap = await self.snap_cloud_service.upload_snap(snap_bytes)
        return SnapResponseModel(
            id=snap_id,
            created_at=datetime.now(),
            snap_url=cloudinary_snap.url,
            **snap_create.dict()
        )
