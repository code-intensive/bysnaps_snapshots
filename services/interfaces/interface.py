from abc import ABCMeta, abstractmethod

from database.models.models import Snap
from models.snaps import SnapCreate, SnapUpdate


class ISnapService(ABCMeta):
    @abstractmethod
    async def create_snap(self, snap_create: SnapCreate) -> Snap:
        ...

    @abstractmethod
    async def get_snaps(self) -> list[Snap]:
        ...

    @abstractmethod
    async def get_snap(self, snap_id: str) -> Snap:
        ...

    @abstractmethod
    async def update_snap(self, snap_update: SnapUpdate) -> None:
        ...

    @abstractmethod
    async def delete_snap(self, snap_id: str) -> None:
        ...
