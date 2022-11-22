from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from database.managers.interfaces.snap_manager_interface import ISnapManager
from database.models.models import Snap, SnapItem
from database.utils.model_converter import snap_from_pydantic
from database.utils.prebuilt_queries import fetch_snap_query, fetch_snaps_query
from models.snaps import SnapInDB, SnapUpdate


class SnapManager(ISnapManager):
    """SnapManager for database related actions"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, orm_snap: SnapInDB) -> Snap:
        snap = await snap_from_pydantic(orm_snap)
        self._session.add(snap)
        await self._session.flush()
        return orm_snap

    async def fetchone(self, snap_id: str) -> Snap:
        snap = await self._session.execute(fetch_snap_query(snap_id))
        snap = snap.scalars().first()
        if snap is None:
            raise HTTPException(HTTP_404_NOT_FOUND, detail="snap not found")
        return snap

    async def fetchall(self) -> list[Snap]:
        snaps = await self._session.execute(fetch_snaps_query())
        return snaps.scalars().fetchall()

    async def update(self, snap_update: SnapUpdate) -> None:
        snap = await self.fetchone(snap_update.id)
        snap.snap_items = [
            SnapItem(**snap_item.dict()) for snap_item in snap_update.snap_items
        ]
        if snap_update.description:
            snap.description = snap_update.description
        snap.last_modified = datetime.now()
        self._session.add(snap)
        await self._session.flush()

    async def delete(self, snap: Snap) -> None:
        return await self._session.delete(snap)
