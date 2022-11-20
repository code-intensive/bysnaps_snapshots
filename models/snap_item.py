from pydantic import BaseModel, Field


class SnapItem(BaseModel):
    item_id: str = Field(
        title="Product",
        description="Universally unique identifier of the snap item",
    )
    quantity: int = Field(
        title="Quantity",
        description="The number of snap_items requested by the user",
    )

    class Config:
        orm_mode = True
