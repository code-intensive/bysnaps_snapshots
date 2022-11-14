from database.models.models import Product, Snap
from models.snaps import SnapInDB


async def snap_from_pydantic(orm_snap: SnapInDB) -> Snap:
    snap_data = orm_snap.dict()
    products_data = snap_data.pop("products")
    products = [Product(**product) for product in products_data]
    return Snap(products=products, **snap_data)
