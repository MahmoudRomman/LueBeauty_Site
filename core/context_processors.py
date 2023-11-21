from . import models


# def get_account_name(user_phone):
#     phone = models.PhoneNumber.objects.get(phone=user_phone)
#     account = models.Account.objects.get(phone_number=phone)
#     return account



# def get_account_name(request, user_phone):
#     phone = models.PhoneNumber.objects.get(phone=user_phone)
#     account = models.Account.objects.get(phone_number=phone)

#     data = {
#         'account' : account
#     }
#     return data