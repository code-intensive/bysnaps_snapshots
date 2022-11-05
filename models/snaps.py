from datetime import datetime

from pydantic import BaseModel, Field

from models.products import Product


class Snap(BaseModel):
    """
    A Snap holds required data for QRCode creation
    """

    products: list[Product] = Field(
        description="list of products selected by the user via this snap"
    )
    description: str | None = Field(
        description="Optional purchase description", max_length=150
    )
    customer_id: str = Field(
        title="Customer",
        description="The Universally unique identifier of the user",
    )
    store_id: str = Field(
        title="Store",
        description="Universally unique identifier of the store",
    )


class ORMSnap(Snap):
    """
    A Snap contains data from a SnapData, this data is used to create QRCode for the requested items and transactions
    """

    id: str
    snap_url: str = Field(description="The public url to a cloudinary image")
    created_at: datetime = Field(
        title="Time of creation", description="The date and time the snap was created"
    )

    class Config:
        orm_mode = True
