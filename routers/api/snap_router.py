from controllers.api.snap_controllers import (
    create_snap,
    get_snap,
    get_snaps,
    health_check,
)
from fastapi.routing import APIRouter
from models.snaps import ORMSnap

snaps_router = APIRouter(prefix="/snap-shots")


snaps_router.add_api_route(
    path="/health",
    endpoint=health_check,
    methods=["get"],
    summary="Service health check",
)

snaps_router.add_api_route(
    path="",
    endpoint=create_snap,
    methods=["post"],
    status_code=201,
    summary="Create a new snap",
)

snaps_router.add_api_route(
    path="",
    endpoint=get_snaps,
    methods=["get"],
    response_model=list[ORMSnap],
    summary="Retrieve all snaps",
)

snaps_router.add_api_route(
    path="/{snap_id: str}",
    endpoint=get_snap,
    methods=["get"],
    response_model=ORMSnap,
    summary="Retrieve a snap by it's id",
)
