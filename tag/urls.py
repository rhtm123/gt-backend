from django.urls import path
from tag import views

urlpatterns = [
    path('tags/', views.TagListCreate.as_view()),
    path('tag/<int:pk>/', views.TagGetUpdate.as_view()),
    path('tag/<str:slug>-<int:pk>/', views.TagGetUpdateSlug.as_view()),
    path('tag/delete/<int:pk>/', views.TagDelete.as_view()),
]