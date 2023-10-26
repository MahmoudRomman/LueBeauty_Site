from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from . import models
from . import forms
from datetime import datetime 
import datetime, calendar

from django.utils import timezone



# Create your views here.

def home(request):
    return render(request, 'core/index.html')


def store(request):
    if request.method == "POST":
        form = forms.ItemForm()
        
        wig_type = request.POST.get("wig_type")
        wig_long = request.POST.get("wig_long")
        scalp_type = request.POST.get("scalp_type")
        wig_color = request.POST.get("wig_color")
        density = request.POST.get("density")

        if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
            data = models.Item.objects.all()
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        else:
            data = models.Item.objects.filter(wig_type = wig_type, wig_long = wig_long,
                                                scalp_type = scalp_type, wig_color = wig_color,
                                                density = density)
            
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/store.html', context)

    else:
        form = forms.ItemForm()
        data = models.Item.objects.all()
        paginator = Paginator(data, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/store.html', context)




def add_product(request):

    form = forms.ProductForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            wig_type = form.cleaned_data.get("wig_type")
            wig_long = form.cleaned_data.get("wig_long")
            scalp_type = form.cleaned_data.get("scalp_type")
            wig_color = form.cleaned_data.get("wig_color")
            density = form.cleaned_data.get("density")
            price = form.cleaned_data.get("price")
            quantity = form.cleaned_data.get("quantity")

            if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
                 messages.info(request, "هناك خطأ من فضلك راجع المدخلات مره أخرى")
            else:
                new_product = models.Product.objects.create(
                    name = name,
                    wig_type = wig_type,
                    wig_long = wig_long,
                    scalp_type = scalp_type,
                    wig_color = wig_color,
                    density = density,
                    price = price,
                    quantity = quantity,
                    )

                new_product.save()
                messages.success(request, "تم اضافة المنتج الجديد بنجاح")
                return redirect("store")



    context = {
        'form' : form,
    }

    return render(request, 'core/add_product.html', context)



import string
import random


def create_slug_code():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=20))

def add_item(request):

    form = forms.ItemForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            wig_type = form.cleaned_data.get("wig_type")
            wig_long = form.cleaned_data.get("wig_long")
            scalp_type = form.cleaned_data.get("scalp_type")
            wig_color = form.cleaned_data.get("wig_color")
            density = form.cleaned_data.get("density")
            price = form.cleaned_data.get("price")
            discount_price = form.cleaned_data.get("discount_price")
            quantity = form.cleaned_data.get("quantity")

            if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
                 messages.warning(request, "هناك خطأ من فضلك راجع المدخلات مره أخرى")
            else:

                check_the_item = models.Item.objects.filter(
                    name = name, wig_type = wig_type,
                    wig_long = wig_long, scalp_type = scalp_type,
                    wig_color = wig_color, density = density,
                    )
                if len(check_the_item) == 0:
                    create_slug = create_slug_code()
                    new_item = models.Item.objects.create(
                        name = name,
                        wig_type = wig_type,
                        wig_long = wig_long,
                        scalp_type = scalp_type,
                        wig_color = wig_color,
                        density = density,
                        price = price,
                        discount_price = discount_price,
                        quantity = quantity,

                        slug = create_slug
                        )

                    new_item.save()
                    messages.success(request, "تم اضافة المنتج الجديد بنجاح")
                    return redirect("store")
                else:
                    messages.warning(request, ".هذ المنتج موجود بالفعل يمكنك تعديل السعر او الكمية له")
                    return redirect("store")

    context = {
        'form' : form,
    }

    return render(request, 'core/add_item.html', context)




def edit_item_in_store(request, slug):
    item = models.Item.objects.get(slug=slug)

    if request.method == "POST":
        form = forms.EditItemForm(request.POST, instance=item)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            wig_type = form.cleaned_data.get("wig_type")
            wig_long = form.cleaned_data.get("wig_long")
            scalp_type = form.cleaned_data.get("scalp_type")
            wig_color = form.cleaned_data.get("wig_color")
            density = form.cleaned_data.get("density")
            price = form.cleaned_data.get("price")
            discount_price = form.cleaned_data.get("discount_price")
            quantity = form.cleaned_data.get("quantity")
            if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
                 messages.warning(request, "هناك خطأ من فضلك راجع المدخلات مره أخرى")
            else:
                models.Item.objects.filter(slug=slug).update(
                    name = name, wig_type = wig_type,
                    wig_long = wig_long, scalp_type = scalp_type,
                    wig_color = wig_color, density = density,
                    price=price, discount_price = discount_price,
                    quantity = quantity)
                
                messages.success(request, "تم تعديل هذا المنتج بنجاح")
                return redirect("store")
    else:
        form = forms.EditItemForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request, 'core/edit_item.html', context)




def delete_from_store(request, slug):
    item = models.Item.objects.get(slug=slug)

    if request.method == "POST":
        item.delete()
        messages.success(request, ".تم ازالة هذا المنتج من المخزن")
        return redirect("store")
    
    return render(request, 'core/delete_item_confirm.html')




def shop(request):
    if request.method == "POST":
        form = forms.ItemForm()
        
        wig_type = request.POST.get("wig_type")
        wig_long = request.POST.get("wig_long")
        scalp_type = request.POST.get("scalp_type")
        wig_color = request.POST.get("wig_color")
        density = request.POST.get("density")

        if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
            data = models.Item.objects.all()
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        else:
            data = models.Item.objects.filter(wig_type = wig_type, wig_long = wig_long,
                                                scalp_type = scalp_type, wig_color = wig_color,
                                                density = density)
            
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/shop.html', context)
    

    else:
        form = forms.ItemForm()
        data = models.Item.objects.all()
        paginator = Paginator(data, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/shop.html', context)
    
    




# This function used to set the item to the cart in addition update the product quantity in the store...
# Done perfectly.....
def add_to_cart(request, slug):

    # get the item
    item = get_object_or_404(models.Item, slug=slug)
    
    # create an order item or that order or get it if it exists
    order_item, created = models.OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the orderitem is in the order
        if order.items.filter(item__slug = item.slug).exists():
            if item.quantity > 0:
                order_item.quantity += 1
                order_item.save()

                # Update the quantity for the item in the cart
                models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))


                messages.success(request, "تم تعديل الكمية لهذا المنتج بنجاح")
                return redirect("order_summary")
            else:
                messages.warning(request, "هذا المنتج خارج المخزن")
                return redirect("shop")
        else:
            if item.quantity > 0:
                order.items.add(order_item)

                # Update the quantity for the item in the cart
                models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

                messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح" )
                return redirect("order_summary")
            else:
                messages.warning(request, "هذا المنتج خارج المخزن")
                return redirect("shop")



    else: 
        if item.quantity > 0:

            # Update the quantity for the item in the cart
            models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

            ordered_date = timezone.now()
            order = models.Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح")
            redirect("shop")

            return redirect("order_summary")
        else:
            messages.warning(request, "هذا المنتج خارج المخزن")
            return redirect("shop")




def remove_single_item_from_cart(request, slug):
    # get the item
    item = get_object_or_404(models.Item, slug=slug)
    
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the orderitem is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()

                # Update the quantity for the item in the cart
                models.Item.objects.filter(slug=slug).update(quantity = (item.quantity + 1))

                messages.success(request, ".تم تعديل الكمية لهذا المنتج")
                return redirect("order_summary")
            else:
                order.items.remove(order_item)
                order_item.save()
                messages.success(request, ".تم ازالة هذا المنتج من السلة")
                return redirect("order_summary")


        else:
            messages.info(request, "!هذا المنتج غير موجود فى السلة")
            return redirect("shop")
    else:
        messages.info(request, "!ليس لديك فاتورة")
        return redirect("shop")
    



def remove_from_cart(request, slug):
    # get the item
    item = get_object_or_404(models.Item, slug=slug)
    
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the orderitem is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            # Update the quantity for the item in the cart
            models.Item.objects.filter(slug=slug).update(quantity = (item.quantity + order_item.quantity))
            
            order.items.remove(order_item)
            messages.success(request, ".تم ازالة هذا المنتج من السلة")
            return redirect("order_summary")

        else:
            messages.info(request, "!هذا المنتج غير موجود فى السلة")
            return redirect("shop", slug=slug)
    else:
        messages.info(request, "!ليس لديك فاتورة")
        return redirect("shop")










def order_summary(request):
    order = models.Order.objects.get(user=request.user, ordered=False)

    context = {
        'object' : order,
        # 'couponform' : forms.CouponForm(),
        # 'DISPLAY_COUPON_FORM' : True,
    }

    return render(request, 'core/order_summary.html', context)


def bill(request):
    return render(request, 'core/bill.html')




def banks(request):

    links_data = models.AddLink.objects.all()


    context = {
        'links_data' : links_data,
    }
    return render(request, 'core/banks.html', context)



def add_payment_link(request):

    form = forms.AddLinkForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            link_name = form.cleaned_data.get("link_name")
            amount = form.cleaned_data.get("amount")
            SAR_link = form.cleaned_data.get("SAR_link")
            AED_link = form.cleaned_data.get("AED_link")


            
            create_slug = create_slug_code()

            new_link = models.AddLink.objects.create(
                link_name = link_name,
                slug_link = create_slug,
                amount = amount,
                SAR_link = SAR_link,
                AED_link = AED_link,
                )

            new_link.save()
            messages.success(request, "تم اضافة الرابط الجديد بنجاح")
            return redirect("banks_and_payments")



    context = {
        'form' : form,
    }

    return render(request, 'core/add_new_link.html', context)



def delete_payment_link(request, slug):
    models.AddLink.objects.filter(slug_link=slug).delete()
    messages.info(request, "item deleted successfully")
    return redirect("banks_and_payments")



def copy_link(request):
    pass


from django.http import JsonResponse





def chart_data(request):

    year = 2023
    month = 10
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    
    randomlist = []
    for i in range(0,30):
        n = random.randint(1,30)
        randomlist.append(n)

    labels = days
    values = randomlist
    
    chart_data = {
        'label': 'خريطة المبيعات الخاصة بك خلال هذا الشهر',
        'labels': labels,
        'values': values,
        'chart_type': 'bar' # any chart type line, bar, ects
    }
    
    return JsonResponse(chart_data)


def chart_view(request):
    return render(request, 'core/chart.html')