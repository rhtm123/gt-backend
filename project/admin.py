from django.contrib import admin

# Register your models here.
from django.utils.html import format_html


from .models import ProjectPackagePayment, Technology, Project, Service, Package, ProjectPackage, ProjectPackageService


admin.site.register(Package)
# admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Service)
# admin.site.register(Coupon)


class ProjectPackageInline(admin.TabularInline):
    model = ProjectPackage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('client',)
    list_filter = ('client',)

    inlines = [ProjectPackageInline,]



admin.site.register(Project, ProjectAdmin)



class ProjectPackageServiceInline(admin.TabularInline):
    model = ProjectPackageService
    extra = 1


class ProjectPackagePaymentInline(admin.TabularInline):
    model = ProjectPackagePayment
    extra = 1

class ProjectPackageAdmin(admin.ModelAdmin):

    list_display = ('project', "package" ,"price", "paid", "print_payment_invoice", "print_payment_receipt")
    def print_payment_invoice(self, obj):
        return format_html(f'<a class="button" target="_blank" href="/project/payment-invoice/{obj.id}">Invoice</a>')

    print_payment_invoice.short_description = 'Action'

    def print_payment_receipt(self, obj):
        return format_html(f'<a class="button" target="_blank" href="/project/payment-receipt/{obj.id}">Receipt</a>')

    print_payment_receipt.short_description = 'Action'

    inlines = (ProjectPackageServiceInline, ProjectPackagePaymentInline) 


admin.site.register(ProjectPackage, ProjectPackageAdmin)
