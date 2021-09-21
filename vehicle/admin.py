from django.contrib import admin
from .models import Vehicle
from products.models import Gps
from django.utils.html import format_html
from django.urls import reverse


class VehicleAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner',)
    list_display = (
        'number',
        'type',
        'make',
        'model',
        'get_link_owner_name',
        'get_link_owner_login',
        'rate_client',
        'rate_price',
        'get_link_gps',
        'get_link_gps_fuel',
    )
    list_filter = (
        'type',
        'make',
        'model',
        'owner__name',
        'owner__login',
        'rate_client',
    )
    search_fields = [
        'number',
        # 'gps__number',
    ]

    def get_link_owner_name(self, obj):
        if obj.owner:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.owner.id), str(obj.owner.name)))
        return '-'

    get_link_owner_name.admin_order_field = 'owner_name'
    get_link_owner_name.short_description = 'Власник назва'

    def get_link_owner_login(self, obj):
        if obj.owner:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.owner.id), str(obj.owner.login)))
        return '-'
    get_link_owner_login.admin_order_field = 'owner_login'
    get_link_owner_login.short_description = 'Власник login'

    def get_link_gps(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.id), str(obj.gps.number)))
        return '-'
    get_link_gps.short_description = 'БР'

    def get_link_gps_fuel(self, obj):
        if obj.fuel_sensor:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:products_fuelsensor_change', args=(fuel_sensor.pk,)), fuel_sensor) for fuel_sensor in obj.fuel_sensor.all()]))
        return '-'

    get_link_gps_fuel.short_description = 'ДВРП'


admin.site.register(Vehicle, VehicleAdmin)
