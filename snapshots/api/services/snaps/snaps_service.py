import asyncio
from datetime import datetime

from snapshots.database.models.models import Snap
from snapshots.models.pydantic.snaps import SnapCreateModel, SnapModel, SnapUpdateModel
from snapshots.protocols.cloudinary.cloud_snap import CloudSnapProtocol
from snapshots.protocols.generators.snap_generator import SnapGeneratorProtocol
from snapshots.protocols.managers.manager import SnapManagerProtocol
from snapshots.utils.id_generator import generate_uuid


class SnapService:
    """SnapService class."""

    def __init__(
        self,
        snap_manager: SnapManagerProtocol,
        snap_generator: SnapGeneratorProtocol,
        snap_cloud_service: CloudSnapProtocol,
    ) -> None:
        self.snap_manager = snap_manager
        self.snap_generator = snap_generator
        self.snap_cloud_service = snap_cloud_service

    async def create_snap(self, snap_create: SnapCreateModel) -> Snap:
        snap = await self._build_snap(snap_create)
        return await self.snap_manager.create(snap)

    async def get_snaps(self) -> list[Snap]:
        return await self.snap_manager.fetchall()

    async def get_snap(self, id: str) -> Snap:
        return await self.snap_manager.fetchone(id)

    async def update_snap(self, id: str, snap_update: SnapUpdateModel) -> None:
        return await self.snap_manager.update(id, snap_update)

    async def delete_snap(self, id: str) -> None:
        snap = await self.get_snap(id)
        await asyncio.gather(
            self.snap_cloud_service.delete_snap(snap),
            self.snap_manager.delete(snap),
        )

    async def _build_snap(self, snap_create: SnapCreateModel) -> SnapModel:
        """Private method for snap building.

        :param snap_create: A pydantic model for request validation.

        :return: A pydantic model mapping to an SQLAlchemy Snap model.

        :rtype: SnapModel.
        """
        id = generate_uuid("snap")
        snap_bytes = self.snap_generator.generate_snap(id)
        cloudinary_snap = await self.snap_cloud_service.upload_snap(snap_bytes)
        return SnapModel(
            id=id,
            created_at=datetime.now(),
            snap_url=cloudinary_snap.url,
            **snap_create.dict()
        )
