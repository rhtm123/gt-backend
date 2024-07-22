# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from .models import BatchPurchase, PaymentReceipt, UserBatch

# from certificate.models import Certificate
# Create your views here.
from .models import ProjectPackage, ProjectPackageService, ProjectPackagePayment

def payment_invoice(request, project_package_id):
    context_dict = {}

    project_package = ProjectPackage.objects.get(id=project_package_id)

    services = ProjectPackageService.objects.filter(project_package=project_package)
    payments = ProjectPackagePayment.objects.filter(project_package=project_package).order_by('due_date')

    context_dict['project_package'] = project_package
    context_dict['payments'] = payments
    context_dict['services'] = services

    # context_dict['total_remaining'] = batch_purchase.total_fee_after_discount - batch_purchase.total_paid;

    return render(request, "payment_invoice.html", context_dict)


def payment_receipt(request, project_package_id):
    context_dict = {}

    project_package = ProjectPackage.objects.get(id=project_package_id)

    services = ProjectPackageService.objects.filter(project_package=project_package)
    payments = ProjectPackagePayment.objects.filter(project_package=project_package).order_by('due_date')

    context_dict['project_package'] = project_package
    context_dict['payments'] = payments
    context_dict['services'] = services

    # context_dict['total_remaining'] = batch_purchase.total_fee_after_discount - batch_purchase.total_paid;

    return render(request, "payment_receipt.html", context_dict)