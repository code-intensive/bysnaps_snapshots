from datetime import datetime
from typing import Any

from fastapi import HTTPException
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from snapshots.database.models.models import Snap, SnapItem
from snapshots.database.utils.model_converter import snap_from_pydantic
from snapshots.database.utils.prebuilt_queries import (
    fetch_snap_query,
    fetch_snaps_query,
)
from snapshots.models.pydantic.snaps import SnapResponseModel, SnapUpdateModel


class SnapManager:
    """SnapManager for database related actions"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, orm_snap: SnapResponseModel) -> Snap:
        snap = snap_from_pydantic(orm_snap)
        self._session.add(snap)
        await self._session.flush()
        return snap

    async def fetchone(self, id: str) -> Snap:
        snap = await self._session.scalars(fetch_snap_query(id))
        if (snap := snap.first()) is None:
            raise HTTPException(HTTP_404_NOT_FOUND, detail="snap not found")
        return snap

    async def fetchall(self) -> AbstractPage[Any]:
        return await paginate(self._session, fetch_snaps_query())

    async def update(self, id: str, snap_update: SnapUpdateModel) -> None:
        snap = await self.fetchone(id)
        SnapManager._update(snap, snap_update)
        self._session.add(snap)
        await self._session.flush()

    async def delete(self, snap: Snap) -> None:
        await self._session.delete(snap)

    @staticmethod
    def _update(snap: Snap, snap_update: SnapUpdateModel) -> None:
        snap.snap_items = [
            SnapItem(**snap_item.dict()) for snap_item in snap_update.snap_items
        ]
        if snap_update.description:
            snap.description = snap_update.description
        snap.last_modified = datetime.now()
