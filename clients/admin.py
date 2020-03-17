from django.contrib import admin
from contracts.models import Contract
from .models import Client, ClientPostAddress, ContactProfile
from vehicle.models import Vehicle


class VehicleInline(admin.StackedInline):
    model = Vehicle
    fields = ('type', 'make', 'model', 'number',)


class ContractInline(admin.StackedInline):
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    inlines = [ContractInline, VehicleInline]
    list_display = ('name', 'login', 'status', 'day_start', 'address',)
    list_filter = ('status',)
    search_fields = ['name', 'login', ]


class ClientPostAddressAdmin(admin.ModelAdmin):
    list_display = ('client', 'index', 'region', 'district', 'city', 'street', 'house', 'office',)
    search_fields = ['client', 'index', 'city', 'region', 'street', ]


class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'surname', 'patronymic', 'position', 'phone', 'phone_2', 'email',)
    list_filter = ('client_field',)
    search_fields = ['firstname', 'phone', 'phone_2', 'email', ]


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientPostAddress, ClientPostAddressAdmin)
admin.site.register(ContactProfile, ContactProfileAdmin)

