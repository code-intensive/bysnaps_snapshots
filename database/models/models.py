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

    last_modified = Column(DateTime)
    description = Column(String(255), index=True)
    created_at = Column(DateTime, nullable=False)
    snap_url = Column(String(150), nullable=False)
    store_id = Column(String(50), index=True, nullable=False)
    customer_id = Column(String(50), index=True, nullable=False)
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
