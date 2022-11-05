from abc import ABCMeta, abstractmethod

from models.snaps import ORMSnap, Snap


class ISnapManager(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, snap_data: ORMSnap) -> Snap:
        """Creates a snap shot from the ORMSnamepShot"""
        ...

    @abstractmethod
    async def fetchone(self, snap_id: str) -> Snap:
        """Retrieves a snap shot from the databases using it's snap id"""
        ...

    @abstractmethod
    async def fetchall(self) -> list[Snap]:
        """Retrieves all snap shots from the database"""
        ...

    @abstractmethod
    async def delete(self, snap_id: str) -> Snap:
        """Deletes a snap shot from the database using it's snap id"""
        ...
