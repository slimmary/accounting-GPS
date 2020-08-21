from django.contrib import admin
from contracts.models import Contract
from .models import Client, ClientPostAddress, ContactProfile
from vehicle.models import Vehicle
from products.models import Gps


class GpsInline(admin.StackedInline):
    list_per_page = 20
    model = Gps
    fields = ('number', 'vehicle', 'rate_client', 'rate_price')


class ContractInline(admin.StackedInline):
    list_per_page = 20
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [ContractInline, GpsInline]
    list_display = (
        'name',
        'login',
        'status',
        'day_start',
        'get_all_gps',
        'address',
    )
    list_filter = ('status',)
    search_fields = ['name', 'login', ]

    def get_all_gps(self, obj):
        queryset = obj.gps.all().count()
        return queryset

    get_all_gps.admin_order_field = 'gps_all'
    get_all_gps.short_description = 'Кількість БР'


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

