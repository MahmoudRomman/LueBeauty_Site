from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Item)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
admin.site.register(models.Bill)
admin.site.register(models.Coupon)

admin.site.register(models.PhoneNumber)
admin.site.register(models.Account)


admin.site.register(models.Product)
admin.site.register(models.AddLink)
