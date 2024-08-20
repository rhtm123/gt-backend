

from .models import Project, ProjectImage
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import ProjectSchema, ProjectImageSchema
# from typing import List

router = Router()


from extra.pagination import PaginatedResponseSchema, paginate_queryset


@router.get("/projects", response=PaginatedResponseSchema)
# @paginate(ProjectNumberPagination)
def projects(request, page: int = Query(1), page_size: int = Query(10)):
    qs = Project.objects.select_related('client').prefetch_related('technology_used').all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, ProjectSchema, page_number, page_size)


@router.get("/projects/{project_id}", response=ProjectSchema)
def project(request, project_id: int):
    project = Project.objects.select_related('client').prefetch_related('technology_used').get(id=project_id)
    return project


@router.get("/project/images/{project_id}", response=PaginatedResponseSchema)
# @paginate(ProjectNumberPagination)
def project_images(request, project_id: int, page: int = Query(1), page_size: int = Query(10)):
    qs = ProjectImage.objects.filter(project=project_id)
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, ProjectImageSchema, page_number, page_size)
