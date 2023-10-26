from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.



wig_name = (
    ('باروكة شعر طبيعى', 'باروكة شعر طبيعى'),
)

wig_type = (
    ("اختر نوع الباروكة", "اختر نوع الباروكة"),
    ('جذور امامية', 'جذور امامية'),
    ('جذور كامله', 'جذور كامله'),
    ('جذور دائرية 360', 'جذور دائرية 360'),

)

wig_long = (
    ("طول الباروكة", "طول الباروكة"),
    ('12 Inch', '12 Inch'),
    ('14 Inch', '14 Inch'),
    ('16 Inch', '16 Inch'),
    ('18 Inch', '18 Inch'),
    ('20 Inch', '20 Inch'),
    ('22 Inch', '22 Inch'),
    ('24 Inch', '24 Inch'),
    ('26 Inch', '26 Inch'),
    ('28 Inch', '28 Inch'),
    ('30 Inch', '30 Inch'),
    ('32 Inch', '32 Inch'),
    ('34 Inch', '34 Inch'),
    ('36 Inch', '36 Inch'),
    ('38 Inch', '38 Inch'),
    ('40 Inch', '40 Inch'),

)


scalp_type = (
    ("اختر نوع الفروة", "اختر نوع الفروة"),
    ('دانتيل', 'دانتيل'),
    ('حرير', 'حرير'),

)


wig_color = (
    ("اختر لون الباروكة", "اختر لون الباروكة"),
    ('أسود طبيعى', 'أسود طبيعى'),
    ('بنى داكن', 'بنى داكن'),
    ('بنى فاتح', 'بنى فاتح'),
    ('اشقر', 'اشقر'),
    ('مخصل', 'مخصل'),

)


density = (
    ('اختر كثافة الباروكة', 'اختر كثافة الباروكة'),
    ('130', '130'),
    ('150', '150'),
    ('200', '200'),
    ('250', '250'),

)




class Item(models.Model):
    name = models.CharField(max_length=150, choices=wig_name, null=False)
    wig_type = models.CharField(max_length=150, choices=wig_type, null=False)
    wig_long = models.CharField(max_length=150, choices=wig_long, null=False)
    scalp_type = models.CharField(max_length=150, choices=scalp_type, null=False)
    wig_color = models.CharField(max_length=150, choices=wig_color, null=False)
    density = models.CharField(max_length=150, choices=density, null=False)
    
    price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])
    # min_price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])
    # max_price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])

    quantity = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    discount_price = models.FloatField(default=0.00, blank=True, null=True)
    slug = models.SlugField()
    


    def __str__(self):
        # return f"{self.id} -- {self.name} -- {self.slug}"
        return f"{self.id} -- {self.slug}"

    


    # def get_absolute_url(self):
    #     return reverse("core:product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug":self.slug})
    
    # def get_remove_from_cart_url(self):
    #   return reverse("core:remove-from-cart", kwargs={"slug":self.slug})
    



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.item.price * self.quantity
    
    def get_total_discount_item_price(self):
        return self.item.discount_price * self.quantity
    
    def get_amount_saved(self):
        return (self.item.price - self.item.discount_price) * self.quantity

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(default=timezone.now())
    done_ordered_time = models.DateTimeField(default=timezone.now())
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total
    


class BillingAddress(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    # country = CountryField(multiple=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)


    def __str__(self):
        return self.user.username





class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField(default=0.00)


    def __str__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length=150, choices=wig_name, null=False)
    wig_type = models.CharField(max_length=150, choices=wig_type, null=False)
    wig_long = models.CharField(max_length=150, choices=wig_long, null=False)
    scalp_type = models.CharField(max_length=150, choices=scalp_type, null=False)
    wig_color = models.CharField(max_length=150, choices=wig_color, null=False)
    density = models.CharField(max_length=150, choices=density, null=False)
    
    price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])
    # min_price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])
    # max_price = models.IntegerField(default=1500, validators=[MaxValueValidator(7000), MinValueValidator(400)])

    quantity = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)



    def __str__(self):
        return f"{self.id} -- {self.name}"





# the model of the add new link to show in the banks and pyament page
class AddLink(models.Model):
    link_name = models.CharField(max_length=150, null=False, blank=False)
    slug_link = models.CharField(max_length=150, unique=True, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    SAR_link = models.URLField(max_length=500, null=False, blank=False)
    AED_link = models.URLField(max_length=500, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)



    def __str__(self):
        return self.slug_link
