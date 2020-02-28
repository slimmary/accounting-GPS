from django.contrib import admin
from apps.contracts.models import Contract
from .models import Client, ClientPostAddress, ContactProfile


class ContractInline(admin.StackedInline):
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    inlines = [ContractInline]


class ClientPostAddressAdmin(admin.ModelAdmin):
    raw_id_fields = ("address",)


class ContactProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("contact_profile",)


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientPostAddress)
admin.site.register(ContactProfile)

