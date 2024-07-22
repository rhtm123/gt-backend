from django.contrib import admin

# Register your models here.

from .models import Coupon

class CouponAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ('user', 'code',  'discount',)
    list_filter = ('user',)



admin.site.register(Coupon, CouponAdmin)