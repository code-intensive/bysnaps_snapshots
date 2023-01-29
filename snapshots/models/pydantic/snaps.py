from datetime import datetime

from pydantic import BaseModel, Field

from snapshots.models.pydantic.snap_item import SnapItem


class BaseSnapModel(BaseModel):
    """Base class for Snap pydantic models."""

    snap_items: list[SnapItem] = Field(
        description="list of snap_item selected by the user via this snap",
    )
    description: str | None = Field(
        description="Optional purchase description",
        max_length=255,
    )


class SnapCreateModel(BaseSnapModel):
    """A Snap holds required data for QRCode creation, used for post."""

    customer_id: str = Field(
        title="Customer",
        description="The Universally unique identifier of the user",
    )
    store_id: str = Field(
        title="Store",
        description="Universally unique identifier of the store",
    )


class SnapUpdateModel(BaseSnapModel):
    """An snap containing id, snap_items and description to be updated."""


class SnapModel(SnapCreateModel):
    """An existing snap matching the database schema,
    containing id, snap_url and created_at.
    """

    id: str
    snap_url: str = Field(description="The public url to a cloudinary image")
    created_at: datetime = Field(
        title="Time of creation",
        description="The date and time the snap was created",
    )
    last_modified: datetime | None = Field(
        title="Time of creation",
        description="The date and time the snap was created",
    )

    class Config:
        orm_mode = True
