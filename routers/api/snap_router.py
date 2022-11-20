from fastapi.routing import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from controllers.api.snap_controllers import (
    create_snap,
    delete_snap,
    get_snap,
    get_snaps,
    health_check,
)
from models.snaps import SnapInDB

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
    status_code=HTTP_201_CREATED,
    summary="Create a new snap",
    response_description="Returns a newly created `SnapInDB`",
)

snaps_router.add_api_route(
    path="",
    endpoint=get_snaps,
    methods=["get"],
    response_model=list[SnapInDB],
    summary="Retrieve all snaps",
)

snaps_router.add_api_route(
    path="/{snap_id}",
    endpoint=get_snap,
    methods=["get"],
    response_model=SnapInDB,
    summary="Retrieve a snap by it's id",
)

snaps_router.add_api_route(
    path="/{snap_id}",
    endpoint=delete_snap,
    methods=["delete"],
    status_code=HTTP_204_NO_CONTENT,
    summary="Delete a snap by it's id",
)
