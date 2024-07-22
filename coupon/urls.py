from django.urls import path

from coupon import views

urlpatterns = [
    path('coupons/', views.CouponListCreate.as_view()),
    path('coupon/<int:pk>/', views.CouponGetUpdate.as_view()),
    path('coupon/code/<str:code>/', views.CouponGetCode.as_view()),
    path('coupon/delete/<int:pk>/', views.CouponDelete.as_view()),
]
