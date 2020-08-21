from django.contrib import admin
from .models import Vehicle
from products.models import Gps


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'make',
        'model',
        'number',
        'get_owner_name',
        'get_owner_login',
        'get_gps',
        'get_gps_fuel',
    )
    list_filter = (
        'type',
        'make',
        'model',
        'gps__owner__name',
        'gps__owner__login',
        'gps__number'
    )
    search_fields = [
        'number',
        'gps__number',
        'owner__login',
        'owner__name',
    ]

    def get_owner_name(self, obj):
        return obj.gps.owner.name
    get_owner_name.admin_order_field = 'owner_name'  # Allows column order sorting
    get_owner_name.short_description = 'Власник назва'  # Renames column head

    def get_owner_login(self, obj):
        return obj.gps.owner.login
    get_owner_login.admin_order_field = 'owner_login'  # Allows column order sorting
    get_owner_login.short_description = 'Власник login'  # Renames column head

    def get_gps(self, obj):
        return obj.gps
    get_gps.short_description = 'БР'

    def get_gps_fuel(self, obj):
        queryset = obj.gps.fuel_sensor.all()
        fuel = [i for i in queryset]
        return fuel
    get_gps_fuel.short_description = 'ДВРП'


admin.site.register(Vehicle, VehicleAdmin)
