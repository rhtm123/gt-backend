

# from .models import Page
from django.contrib.auth.models import User

from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import UserSchemaIn, UserSchemaOut

from django.contrib.auth.hashers import make_password

from ninja.errors import HttpError


# from typing import List

router = Router()


from extra.pagination import PaginatedResponseSchema, paginate_queryset


@router.get("users", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def users(request, page: int = Query(1), page_size: int = Query(10)):
    qs = User.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, UserSchemaOut, page_number, page_size)


@router.get("users/{id}", response=UserSchemaOut)
def userbyid(request, id: int):
    obj = get_object_or_404(User, id=id)
    return obj

@router.get("users/email/{email}", response=UserSchemaOut)
def userbyemail(request, email: str):
    obj = get_object_or_404(User, email=email)
    return obj


@router.post("users/create/")
def create_user(request, user_data: UserSchemaIn):
    try:
        user_data = user_data.dict();
        print(user_data)
        user = User.objects.create(
            username=user_data.get("email"),
            first_name = user_data.get('first_name'),
            last_name = user_data.get('last_name'),
            password=make_password(user_data.get("password")),  # Hash the password
            email=user_data.get("email"),
        )
        return {"success": True, "id": user.id, "message": "User created successfully!"}
    except:
        raise HttpError(400, "A user with this username already exists.")
        # return {"success": False, "message": "A user with this username already exists."}
