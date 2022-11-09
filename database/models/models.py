from database.config.setup import Model
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from utils.id_generator import generate_uuid

CASCADE = "CASCADE"


class Product(Model):
    __tablename__ = "products"

    id = Column(String(50), primary_key=True, default=lambda: generate_uuid("product"))
    quantity = Column(Integer)
    product_id = Column(String(50), index=True)
    snap = relationship("Snap", back_populates="products")
    snap_id = Column(String(50), ForeignKey("snaps.id", ondelete=CASCADE))

    __mapper_args__ = {"eager_defaults": True}


class Snap(Model):
    __tablename__ = "snaps"

    snap_url = Column(String(100))
    created_at = Column(DateTime)
    store_id = Column(String(50), index=True)
    customer_id = Column(String(50), index=True)
    description = Column(String(255), index=True)
    id = Column(
        String(50),
        primary_key=True,
        index=True,
        default=lambda: generate_uuid("snap"),
    )
    products = relationship(
        "Product",
        back_populates="snap",
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {"eager_defaults": True}
