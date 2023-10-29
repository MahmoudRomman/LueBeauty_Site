from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from . import models





class ProductForm(forms.Form):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',

    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        
    }))



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '500',
        'max' : '7000',
        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        }))
    



    


class ItemForm(forms.Form):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

#         width: 100%;
#   padding:10px;
#   border-radius:10px;

    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'style': 'border-color:wightblack; border-radius: 10px;'


    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        'style': 'border-color:wightblack; border-radius: 10px;'

        
    }))



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '500',
        'max' : '7000',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم",
        'default' :  '0.00',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    






class EditItemForm(forms.ModelForm):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',

    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        
    }))



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '500',
        'max' : '7000',
        }))
    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم",
        'default' :  '0.00',
        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        }))
    

    class Meta:
         model = models.Item
         fields = ['name', 'wig_type', 'wig_long', 'scalp_type', 'wig_color', 'density', 'price', 'discount_price', 'quantity']




class AddLinkForm(forms.Form):
        link_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "150",
        'placeholder': "Stripe اسم لينك الدفع, مثال",
        'style': 'border-color:wightblack; border-radius: 10px;',

        }))

        amount = forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخال مبلغ الدفع",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        SAR_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع السعودى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        AED_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع الاماراتى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))




from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


# class BillForm(forms.Form):


#     country = CountryField(blank_label="(اختر الدولة)").formfield(
#         widget=CountrySelectWidget(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'style': 'border-color:wightblack; border-radius: 10px;'

#             }))
    

#     address = forms.CharField(required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'type' : 'text',
#         'size': "200",
#         'placeholder': "ادخل العنوان",
#         'style': 'border-color:wightblack; border-radius: 10px;'
#     }))

#     customer_phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'size': "31",
#         'placeholder': "ادخل رقم هاتف العميل",
#         'style': 'border-color:wightblack; border-radius: 10px;',

#     }))

#     # seller_phone = forms.ChoiceField(
#     #     choices = models.PhoneNumber.get_phones,
#     #     required = True,
#     #     widget = forms.Select(attrs={
#     #     'class': 'form-control',
#     #     'type' : 'radio',
#     #     'label' : 'select one',
        
#     # }))




class BillForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["country"].widget.attrs.update({
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 10px;'

                })
        

        self.fields["address"].widget.attrs.update({
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 10px;'
        })

        self.fields["customer_phone"].widget.attrs.update({
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 10px;',

        })

        # seller_phone = forms.ChoiceField(
        #     choices = models.PhoneNumber.get_phones,
        #     required = True,
        #     widget = forms.Select(attrs={
        #     'class': 'form-control',
        #     'type' : 'radio',
        #     'label' : 'select one',
            
        # }))

    class Meta:
         model = models.Bill
         fields = ['country', 'address', 'customer_phone']

