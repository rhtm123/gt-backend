"""
URL configuration for gtbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include

from django.conf import settings
from django.conf.urls.static import static


from page.api import router as page_router

from project.api import router as project_router
from builder.api import router as builder_api
from account.api import router as account_api

from ninja import NinjaAPI

api = NinjaAPI()

# api.add_router("blog/", blog_router)
api.add_router("page/", page_router)
api.add_router("project/", project_router)
api.add_router("builder/", builder_api)
api.add_router("user/", account_api)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/', api.urls),
    path('project/', include('project.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
