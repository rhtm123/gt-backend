

from .models import Builder, Project
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import BuilderSchemaOut, ProjectSchemaOut
# from typing import List

router = Router()


from extra.pagination import PaginatedResponseSchema, paginate_queryset



@router.get("/projects", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def projects(request, page: int = Query(1), page_size: int = Query(10)):
    qs = Project.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, ProjectSchemaOut, page_number, page_size)


@router.get("/projects/{page_id}", response=ProjectSchemaOut)
def project(request, page_id: int):
    page = get_object_or_404(Project, id=page_id)
    return page



@router.get("/builders", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def builders(request, page: int = Query(1), page_size: int = Query(10)):
    qs = Builder.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, BuilderSchemaOut, page_number, page_size)


@router.get("/builders/{page_id}", response=BuilderSchemaOut)
def builder(request, page_id: int):
    page = get_object_or_404(Builder, id=page_id)
    return page



