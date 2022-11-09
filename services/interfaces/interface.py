from abc import ABCMeta, abstractmethod

from database.models.models import Snap
from models.snaps import Snap as RawSnap


class ISnapService(ABCMeta):
    @abstractmethod
    async def create_snap(self, raw_snap: RawSnap) -> Snap:
        ...

    @abstractmethod
    async def get_snaps(self) -> list[Snap]:
        ...

    @abstractmethod
    async def get_snap(self, snap_id: str) -> Snap:
        ...

    @abstractmethod
    async def delete_snap(self, snap_id: str) -> None:
        ...
