from datetime import datetime

from models.products import Product
from pydantic import BaseModel, Field


class SnapCreate(BaseModel):
    """
    A Snap holds required data for QRCode creation, used for post
    """

    products: list[Product] = Field(
        description="list of products selected by the user via this snap",
    )
    description: str | None = Field(
        description="Optional purchase description",
        max_length=255,
    )
    customer_id: str = Field(
        title="Customer",
        description="The Universally unique identifier of the user",
    )
    store_id: str = Field(
        title="Store",
        description="Universally unique identifier of the store",
    )


class SnapUpdate(SnapCreate):
    """
    An snap containing id to be updated
    """

    id: str


class SnapInDB(SnapCreate):
    """
    An existing snap matching the database schema,
    containing id, snap_url and created_at
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
