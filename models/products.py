from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: str = Field(
        title="Product",
        description="Universally unique identifier of the product to purchase",
    )
    quantity: int = Field(
        title="Quantity", description="The number of products requested by the user"
    )

    class Config:
        orm_mode = True
