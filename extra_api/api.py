
# from .models import Builder, Project, ClassAllValues
from ninja import  Router, Query
from django.shortcuts import get_object_or_404
# from .schema import BuilderSchemaOut, ProjectSchemaOut, ProjectSchemaIn, ClassAllValuesSchemaOut
# from typing import List

# from django.contrib.auth import get_user_model

# User = get_user_model()
from typing import Optional

# from bs4 import BeautifulSoup
from pydantic import BaseModel
# from extra.builder import determine_key

from django.http import HttpResponsePermanentRedirect, HttpResponse

from domain.models import AllowedDomain

from utils.send_email import send_mail_thread


router = Router()

from decouple import config
 

# from extra.pagination import PaginatedResponseSchema, paginate_queryset

@router.get("/contact", )
def class_all_values_get(request, domain: str, name:str, html_content:str):
    try:
        domain = AllowedDomain.objects.get(domain=domain)
        # print(domain)
        if domain.emails:
            email_list = domain.emails.split(",")

            subject, from_email, to = f'GrowTech notification : {name} has contacted', config('EMAIL_HOST_USER'), email_list

            text_content = f'GrowTech notification : {name} has contacted'

            send_mail_thread(subject=subject, body=text_content,
                            from_email=from_email, recipient_list=to, html=html_content)
            
            return {"success":True}
        else:
            return HttpResponse("Email not available", status=404)

    except:
        return HttpResponse("Not found", status=404)
