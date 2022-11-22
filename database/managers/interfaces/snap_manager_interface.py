from abc import ABCMeta, abstractmethod

from models.snaps import SnapInDB, SnapUpdate


class ISnapManager(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, snap_data: SnapInDB) -> SnapInDB:
        """Creates a snap shot from the ORMSnamepShot"""
        ...

    @abstractmethod
    async def fetchone(self, snap_id: str) -> SnapInDB:
        """Retrieves a snap shot from the databases using it's snap id"""
        ...

    @abstractmethod
    async def fetchall(self) -> list[SnapInDB]:
        """Retrieves all snap shots from the database"""
        ...

    @abstractmethod
    async def update(self, snap_update: SnapUpdate) -> None:
        """Updates a snap shot in the database"""
        ...

    @abstractmethod
    async def delete(self, snap: SnapInDB) -> None:
        """Deletes a snap shot from the database using it's snap id"""
        ...
