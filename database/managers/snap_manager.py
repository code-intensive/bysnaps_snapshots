from database.managers.interfaces.snap_manager_interface import ISnapManager
from database.models.models import Snap
from database.utils.model_converter import snap_from_pydantic
from database.utils.prebuilt_queries import fetch_snap_query, fetch_snaps_query
from fastapi import HTTPException
from models.snaps import SnapInDB
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND


class SnapManager(ISnapManager):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, orm_snap: SnapInDB) -> Snap:
        snap = await snap_from_pydantic(orm_snap)
        self._session.add(snap)
        await self._session.flush()
        return orm_snap

    async def fetchone(self, snap_uuid: str) -> Snap:
        """Retrieves all snap shots from the database"""
        snap = await self._session.execute(fetch_snap_query(snap_uuid))
        snap = snap.scalars().first()
        if snap is None:
            detail = [
                {
                    "loc": [
                        "snap_manager",
                        "get_snap",
                    ],
                    "type": "snap.exceptions.not_found",
                    "msg": "snap not found",
                },
            ]
            raise HTTPException(HTTP_404_NOT_FOUND, detail=detail)
        return snap

    async def fetchall(self) -> list[Snap]:
        """Retrieves all snap shots from the database"""
        snaps = await self._session.execute(fetch_snaps_query())
        return snaps.scalars().fetchall()

    async def delete(self, snap: Snap) -> None:
        """Deletes a snap shot from the databases using it's snap id"""
        return await self._session.delete(snap)
