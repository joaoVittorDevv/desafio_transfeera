from django.contrib import admin
from .models.model_bank import Bank, Agency, Account
from .models.model_receiver import Receiver

admin.site.register(Bank)
admin.site.register(Agency)
admin.site.register(Account)
admin.site.register(Receiver)
