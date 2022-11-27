from datetime import datetime
from typing import Any

from fastapi import HTTPException
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from snapshots.database.managers.interfaces.snap_manager_interface import ISnapManager
from snapshots.database.models.models import Snap, SnapItem
from snapshots.database.utils.model_converter import snap_from_pydantic
from snapshots.database.utils.prebuilt_queries import (
    fetch_snap_query,
    fetch_snaps_query,
)
from snapshots.models.snaps import SnapResponseModel, SnapUpdate


class SnapManager(ISnapManager):
    """SnapManager for database related actions"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, orm_snap: SnapResponseModel) -> Snap:
        snap = await snap_from_pydantic(orm_snap)
        self._session.add(snap)
        await self._session.flush()
        return orm_snap

    async def fetchone(self, snap_id: str) -> Snap:
        snap = await self._session.scalars(fetch_snap_query(snap_id))
        if (snap := snap.first()) is None:
            raise HTTPException(HTTP_404_NOT_FOUND, detail="snap not found")
        return snap

    async def fetchall(self) -> AbstractPage[Any]:
        return await paginate(self._session, fetch_snaps_query())

    async def update(self, snap_update: SnapUpdate) -> None:
        snap = await self.fetchone(snap_update.id)
        self._update(snap, snap_update)
        self._session.add(snap)
        await self._session.flush()

    async def delete(self, snap: Snap) -> None:
        return await self._session.delete(snap)

    def _update(self, snap: Snap, snap_update: SnapUpdate) -> None:
        snap.snap_items = [
            SnapItem(**snap_item.dict()) for snap_item in snap_update.snap_items
        ]
        if snap_update.description:
            snap.description = snap_update.description
        snap.last_modified = datetime.now()
