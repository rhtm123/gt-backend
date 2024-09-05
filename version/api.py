
from ninja.pagination import paginate
from typing import List
from django.shortcuts import get_object_or_404
from .models import Version

from .schema import VersionSchema, VersionIn

from ninja import  Router, Query

from extra.pagination import PaginatedResponseSchema, paginate_queryset


router = Router()


@router.get("/versions", response=PaginatedResponseSchema)
def list_versions(request, page: int = Query(1), page_size: int = Query(10), app_name: str = None, search: str = None, ordering: str = None):
    queryset = Version.objects.all()
    
    if app_name:
        queryset = queryset.filter(app_name=app_name)
    if search:
        queryset = queryset.filter(name__icontains=search) | queryset.filter(detail__icontains=search)
    if ordering:
        queryset = queryset.order_by(ordering)

    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, queryset, VersionSchema, page_number, page_size)

    
# @router.post("/versions", response=VersionSchema)
# def create_version(request, payload: VersionIn):
#     version = Version.objects.create(**payload.dict())
#     return version

@router.get("/versions/{version_id}", response=VersionSchema)
def get_version(request, version_id: int):
    return get_object_or_404(Version, id=version_id)

@router.put("/versions/{version_id}", response=VersionSchema)
def update_version(request, version_id: int, payload: VersionIn):
    version = get_object_or_404(Version, id=version_id)
    for attr, value in payload.dict().items():
        setattr(version, attr, value)
    version.save()
    return version

# @router.get("/versions/{slug}", response=VersionSchema)
# def get_version_by_slug(request, slug: str):
#     return get_object_or_404(Version, slug=slug)

@router.delete("/versions/{version_id}")
def delete_version(request, version_id: int):
    version = get_object_or_404(Version, id=version_id)
    version.delete()
    return {"success": True}

# ... existing code ...