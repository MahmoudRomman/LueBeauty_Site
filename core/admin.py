from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Item)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
admin.site.register(models.BillingAddress)
admin.site.register(models.Coupon)

admin.site.register(models.Product)
admin.site.register(models.AddLink)
