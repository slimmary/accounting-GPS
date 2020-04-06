from django.contrib import admin
from contracts.models import Contract
from .models import Client, ClientPostAddress, ContactProfile
from vehicle.models import Vehicle


class VehicleInline(admin.StackedInline):
    list_per_page = 20
    model = Vehicle
    fields = ('type', 'make', 'model', 'number', 'get_gps', )
    readonly_fields = ('get_gps',)

    def get_gps(self, obj):
        return obj.gps
    get_gps.short_description = 'БР'


class ContractInline(admin.StackedInline):
    list_per_page = 20
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [ContractInline, VehicleInline]
    list_display = ('name', 'login', 'status', 'day_start', 'address',)
    list_filter = ('status',)
    search_fields = ['name', 'login', ]


class ClientPostAddressAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('client', 'index', 'region', 'district', 'city', 'street', 'house', 'office',)
    search_fields = ['client', 'index', 'city', 'region', 'street', ]


class ContactProfileAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('firstname', 'surname', 'patronymic', 'position', 'phone', 'phone_2', 'email',)
    list_filter = ('client_field',)
    search_fields = ['firstname', 'phone', 'phone_2', 'email', ]


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientPostAddress, ClientPostAddressAdmin)
admin.site.register(ContactProfile, ContactProfileAdmin)

