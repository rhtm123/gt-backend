

from .models import Project
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import ProjectSchema
# from typing import List

router = Router()


from extra.pagination import PaginatedResponseSchema, paginate_queryset


# @router.get("/projects", response=PaginatedResponseSchema)
# # @paginate(ProjectNumberPagination)
# def projects(request, page: int = Query(1), page_size: int = Query(10)):
#     qs = Project.objects.all()
#     page_number = request.GET.get('page', 1)
#     page_size = request.GET.get('page_size', 10)

#     return paginate_queryset(request, qs, ProjectSchema, page_number, page_size)


# @router.get("/projects/{page_id}", response=ProjectSchema)
# def blog(request, project_id: int):
#     project = get_object_or_404(Project, id=project_id)
#     return project