from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.config.setup import Model
from utils.id_generator import generate_uuid

CASCADE = "CASCADE"


class SnapItem(Model):
    """SQLAlchemy ORM for snap_items."""

    __tablename__ = "snap_items"

    id = Column(
        String(50),
        primary_key=True,
        default=lambda: generate_uuid("snap_item"),
    )
    quantity = Column(Integer)
    item_id = Column(String(50), index=True)
    snap = relationship("Snap", back_populates="snap_items")
    snap_id = Column(String(50), ForeignKey("snaps.id", ondelete=CASCADE))

    __mapper_args__ = {"eager_defaults": True}


class Snap(Model):
    """SQLAlchemy ORM for snap."""

    __tablename__ = "snaps"

    last_modified = Column(DateTime)
    description = Column(String(255))
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
    snap_items = relationship(
        "SnapItem",
        back_populates="snap",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    __mapper_args__ = {"eager_defaults": True}
