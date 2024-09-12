

from .models import Builder, Project, ClassAllValues
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
from .schema import BuilderSchemaOut, ProjectSchemaOut, ProjectSchemaIn, ClassAllValuesSchemaOut
# from typing import List

from django.contrib.auth import get_user_model

User = get_user_model()
from typing import Optional

from bs4 import BeautifulSoup
from pydantic import BaseModel
from extra.builder import determine_key

from django.http import HttpResponsePermanentRedirect


router = Router()

from extra.pagination import PaginatedResponseSchema, paginate_queryset



@router.get("/class-all-values", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def class_all_values_list(request, page: int = Query(1), page_size: int = Query(10)):
    qs = ClassAllValues.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    return paginate_queryset(request, qs, ClassAllValuesSchemaOut, page_number, page_size)

@router.get("/class-all-values/{name}", response=ClassAllValuesSchemaOut)
def class_all_values_get(request, name: str):
    obj = get_object_or_404(ClassAllValues, name=name)
    return obj



def get_creator(creator_info: Optional[int]):
    if creator_info is None:
        return None
    else:  # Assume it's a username
        return get_object_or_404(User, id=creator_info)
    

@router.get("/projects", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def projects(request, page: int = Query(1), page_size: int = Query(10), creator_id: int = Query(None)):
    qs = Project.objects.all()

    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    if creator_id:
        qs = qs.filter(creator=creator_id)
    return paginate_queryset(request, qs, ProjectSchemaOut, page_number, page_size)


@router.post("/projects/", response=ProjectSchemaOut)
def create_project(request, data: ProjectSchemaIn):
    print(data)
    creator = get_creator(data.creator)

    if data.jsondom is None:
        data.jsondom = r"""
        {
            "type": "div",
            "id": "1",
            "attributes": {
                "class": ""
            },
            "styles": {
            },
            "children": []
        }
        """

    project = Project.objects.create(
        name=data.name,
        jsondom=data.jsondom,
        # is_published=data.is_published,
        creator=creator,
    )
    print("created")
    return project

@router.get("/projects/{project_id}", response=ProjectSchemaOut)
def project(request, project_id: int):
    projectObject = get_object_or_404(Project, id=project_id)
    return projectObject


@router.put("/projects/{project_id}/", response=ProjectSchemaOut)
def update_project(request, project_id: int, data: ProjectSchemaIn):
    print(data)
    project = get_object_or_404(Project, id=project_id)
    
    if data.name is not None:
        project.name = data.name
    if data.jsondom is not None:
        project.jsondom = data.jsondom
    if data.is_published is not None:
        project.is_published = data.is_published
    if data.creator is not None:
        project.creator = get_creator(data.creator)
    
    project.save()
    return project


@router.delete("/projects/{project_id}/")
def delete_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return {"success": True}


@router.get("/builders", response=PaginatedResponseSchema)
# @paginate(PageNumberPagination)
def builders(request, page: int = Query(1), page_size: int = Query(10), creator_id: int = Query(None)):
    qs = Builder.objects.all()
    if creator_id is not None:
        qs = qs.filter(creator=creator_id)
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, BuilderSchemaOut, page_number, page_size)


@router.get("/builders/{builder_id}", response=BuilderSchemaOut)
def builder(request, builder_id: int):
    builderObject = get_object_or_404(Builder, id=builder_id)
    return builderObject


@router.delete("/builders/{builder_id}/")
def delete_Builder(request, builder_id: int):
    obj = get_object_or_404(Builder, id=builder_id)
    obj.delete()
    return {"success": True}




class HTMLInput(BaseModel):
    html: str




def html_to_json(html):
    id_counter = 1

    def to_json(element):
        nonlocal id_counter

        # Handle text nodes
        if isinstance(element, str):
            trimmed_value = element.strip()
            if trimmed_value:
                return {"type": "text", "id": id_counter, "value": trimmed_value}
            return None

        # Handle element nodes
        json_data = {
            "type": element.name,
            "id": id_counter,
            "attributes": get_attributes(element),
            "styles": get_styles(element),
            "children": [],
        }
        id_counter += 1

        for child in element.children:
            child_json = to_json(child)
            if child_json:
                json_data["children"].append(child_json)

        return json_data

    def get_attributes(element):
        attributes = {"class": ""}
        for attr, value in element.attrs.items():
            if attr != "class":
                attributes[attr] = value
        return attributes

    def get_styles(element):
        styles = {}
        class_list = element.get("class", [])
        for class_name in class_list:
            # print(class_name) md:text-lg text-xl
            values = class_name.split(":")
            if len(values)==1:
                key = determine_key(class_name)
                styles[key] = class_name
            else:
                prefix, class_value = values[0],values[1]
                key = determine_key(class_value)
                styles[prefix+":"+key] = class_name
            # print(class_name, key, class_name)
        # print(styles)
        return styles
    
    # Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find all top-level elements
    root_elements = soup.find_all(recursive=False)

    if len(root_elements) == 1:
        # If there's exactly one root element, convert it to JSON
        return to_json(root_elements[0])
    elif len(root_elements) == 0:
        return {"error": "No root element found in the provided HTML."}
    else:
        return {"error": "Multiple root elements found. Only one root element is allowed."}


@router.post("/convert-html-to-json/")
def convert_html_to_json(request, data: HTMLInput):
    json_data = html_to_json(data.html)
    return json_data