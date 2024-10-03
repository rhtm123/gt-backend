
from django.urls import path

from project.views import *


urlpatterns = [
    path('payment-invoice/<int:project_package_id>', payment_invoice),
    path('payment-receipt/<int:project_package_id>', payment_receipt),
    path('payment-quotation/<int:project_package_id>', payment_quotation),

] 