
from .models import Page
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import PageSchemaOut
# from typing import List

router = Router()


from extra.pagination import PaginatedResponseSchema, paginate_queryset


@router.get("/pages", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def pages(request, page: int = Query(1), page_size: int = Query(10)):
    qs = Page.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, PageSchemaOut, page_number, page_size)


@router.get("/pages/{page_id}", response=PageSchemaOut)
def blog(request, page_id: int):
    page = get_object_or_404(Page, id=page_id)
    return page