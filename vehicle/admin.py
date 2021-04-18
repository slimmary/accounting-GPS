from django.contrib import admin
from .models import Vehicle
from products.models import Gps
from django.utils.html import format_html
from django.urls import reverse


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'type',
        'make',
        'model',
        'get_link_owner_name',
        'get_link_owner_login',
        'get_link_gps',
        'get_link_gps_fuel',
    )
    list_filter = (
        'type',
        'make',
        'model',
        'gps__owner__name',
        'gps__owner__login',
    )
    search_fields = [
        'number',
        'gps__number',
    ]

    def get_link_owner_name(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.owner.id), str(obj.gps.owner.name)))
        return '-'
    get_link_owner_name.admin_order_field = 'owner_name'  # Allows column order sorting
    get_link_owner_name.short_description = 'Власник назва'  # Renames column head

    def get_link_owner_login(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.owner.id), str(obj.gps.owner.login)))
        return '-'
    get_link_owner_login.admin_order_field = 'owner_login'  # Allows column order sorting
    get_link_owner_login.short_description = 'Власник login'  # Renames column head

    def get_link_gps(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.id), str(obj.gps.number)))
        return '-'
    get_link_gps.short_description = 'БР'

    def get_link_gps_fuel(self, obj):
        if obj.gps:
            if obj.gps.fuel_sensor:
                return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                    'admin:products_fuelsensor_change', args=(fuel_sensor.pk,)), fuel_sensor) for fuel_sensor in obj.gps.fuel_sensor.all()]))
            return '-'
        return '-'

    get_link_gps_fuel.short_description = 'ДВРП'


admin.site.register(Vehicle, VehicleAdmin)
