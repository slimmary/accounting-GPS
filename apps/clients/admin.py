from django.contrib import admin

from .models import Client, ClientPostAddress, ContactProfile


class ClientAdmin(admin.ModelAdmin):
    raw_id_fields = ("client",)


class ClientPostAddressAdmin(admin.ModelAdmin):
    raw_id_fields = ("address",)


class ContactProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("contact_profile",)


admin.site.register(Client)
admin.site.register(ClientPostAddress)
admin.site.register(ContactProfile)

