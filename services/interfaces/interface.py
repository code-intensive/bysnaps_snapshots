from abc import ABCMeta, abstractmethod

from database.models.models import Snap
from models.snap_data import SnapData


class ISnapService(ABCMeta):
    @abstractmethod
    async def create_snap(self, snap_data: SnapData) -> Snap:
        ...

    @abstractmethod
    async def get_snaps(self) -> list[Snap]:
        ...

    @abstractmethod
    async def get_snap(self, snap_id: str) -> Snap:
        ...
