from controllers.api.snap_controllers import (
    create_snap,
    get_snap,
    get_snaps,
    health_check,
)
from fastapi.routing import APIRouter
from models.snaps import DBSnap

snaps_router = APIRouter(prefix="/snap-shots")


snaps_router.add_api_route(
    path="/health-check",
    endpoint=health_check,
    methods=["get"],
    summary="Service health check",
    response_description=(
        "Returns `null`, it simply shows "
        "that the service is up with a HTTP_200_OK status code"
    ),
)

snaps_router.add_api_route(
    path="",
    endpoint=create_snap,
    methods=["post"],
    status_code=201,
    summary="Create a new snap",
    response_description="Returns a newly created `DBSnap`",
)

snaps_router.add_api_route(
    path="",
    endpoint=get_snaps,
    methods=["get"],
    response_model=list[DBSnap],
    summary="Retrieve all snaps",
)

snaps_router.add_api_route(
    path="/{snap_id}",
    endpoint=get_snap,
    methods=["get"],
    response_model=DBSnap,
    summary="Retrieve a snap by it's id",
)
