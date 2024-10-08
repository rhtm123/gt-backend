from django.contrib import admin

# Register your models here.
from django.utils.html import format_html


from django_summernote.admin import SummernoteModelAdmin

from .models import ProjectImage, ProjectPackagePayment, Technology, Project, Service, Package, ProjectPackage, ProjectPackageService

# from extra.nginx_config import delete_nginx_config, reload_nginx

# import logging

# logger = logging.getLogger(__name__)




admin.site.register(Package)
# admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Service)
# admin.site.register(Coupon)


class ProjectPackageInline(admin.TabularInline):
    model = ProjectPackage
    extra = 1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('name', 'client', 'published', 'domain_validity', 'created')
    list_filter = ('client', 'published')
    search_fields = ('name',)
    list_editable = ('published', 'domain_validity')
    inlines = [ProjectPackageInline,ProjectImageInline]

    
    summernote_fields = ('description',)  # Add this line

admin.site.register(Project, ProjectAdmin)

admin.site.register(ProjectImage)


class ProjectPackageServiceInline(admin.TabularInline):
    model = ProjectPackageService
    extra = 1


class ProjectPackagePaymentInline(admin.TabularInline):
    model = ProjectPackagePayment
    extra = 1

class ProjectPackageAdmin(admin.ModelAdmin):

    list_display = ('project', "package", "price", "paid", "print_payment_invoice", "print_payment_receipt", "print_payment_quotation")

    def print_payment_quotation(self,obj):
        return format_html(f'<a class="button" target="_blank" href="/project/payment-quotation/{obj.id}">Quotation</a>')

    def print_payment_invoice(self, obj):
        return format_html(f'<a class="button" target="_blank" href="/project/payment-invoice/{obj.id}">Invoice</a>')

    print_payment_invoice.short_description = 'Action'

    def print_payment_receipt(self, obj):
        return format_html(f'<a class="button" target="_blank" href="/project/payment-receipt/{obj.id}">Receipt</a>')

    print_payment_receipt.short_description = 'Action'
    inlines = (ProjectPackageServiceInline, ProjectPackagePaymentInline)


admin.site.register(ProjectPackage, ProjectPackageAdmin)

