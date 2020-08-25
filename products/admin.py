from django.contrib import admin
from .models import Sim, Gps, FuelSensor
from django.utils.html import format_html


class SimInline(admin.StackedInline):
    list_per_page = 20
    model = Sim
    fields = ('operator',
              'number',
              'account_number',
              'date_receive',
              )


class GpsAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [SimInline]
    fields = ('number', 'owner', 'vehicle', 'rate_client',)
    list_display = (
        'number',
        'get_gps_fuel',
        'vehicle',
        'link_to_owner_name',
        'link_to_owner_login',
        'get_sim_numb',
        'rate_client'
    )

    list_filter = (
        'number',
        'owner__name',
        'owner__login',
    )
    search_fields = [
        'number',
        'owner__name',
        'owner__login',
        'number',
        'sim__number',
    ]

    def link_to_owner_name(self, obj):
        if obj.owner is None:
            return 'CKT'
        elif obj.owner.id:
            return format_html(
                "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.owner.id), str(obj.owner.name)))
        else:
            return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник назва'

    def link_to_owner_login(self, obj):
        if obj.owner is None:
            return 'CKT'
        elif obj.owner.id:
            return format_html(
                "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.owner.id), str(obj.owner.login)))
        else:
            return 'CKT'

    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Власник Login'

    def get_sim_numb(self, obj):
        queryset = obj.sim.all()
        sim = [i.number for i in queryset]
        return sim
    get_sim_numb.short_description = 'Сім-Картки номер'

    def get_gps_fuel(self, obj):
        queryset = obj.fuel_sensor.all()
        fuel = [i for i in queryset]
        return fuel
    get_gps_fuel.short_description = 'ДВРП'


class SimAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = (
        'operator',
        'account_number',
        'gps',
        'installer',
        'date_given',
        'gps__owner__login',
    )
    search_fields = ['number', 'gps__number']
    list_display = (
        'get_operator',
        'number',
        'account_number',
        'date_receive',
        'installer',
        'date_given',
        'link_to_owner_name',
        'link_to_owner_login',
    )

    def link_to_owner_name(self,obj):
        if obj.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.gps.owner.id), str(obj.gps.owner.name)))
            else:
                return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник назва'

    def link_to_owner_login(self, obj):
        if obj.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.gps.owner.id), str(obj.gps.owner.login)))
            else:
                return 'CKT'
    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Власник Login'

    def get_operator(self, obj):
        return obj.get_operator_display()
    get_operator.admin_order_field = 'operator'
    get_operator.short_description = 'Оператор'


class FuelSensorAdmin(admin.ModelAdmin):
    list_per_page = 20
    fields = ('serial', 'number', 'date_manufacturing', 'gps')
    list_display = (
        'serial',
        'number',
        'date_manufacturing',
        'get_gps_number',
        'get_gps_vehicle',
        'link_to_owner_name',
        'link_to_owner_login',
    )
    list_filter = (
        'date_manufacturing',
        'gps',
        'gps__owner__name',
        'gps__owner__login',
    )
    search_fields = [
        'number',
        'gps__number',
        'gps__owner__login',
    ]

    def get_gps_number(self, obj):
        return obj.gps.number
    get_gps_number.admin_order_field = 'gps_number'
    get_gps_number.short_description = 'БР'

    def get_gps_vehicle(self, obj):
        return obj.gps.vehicle
    get_gps_vehicle.admin_order_field = 'gps_vehicle'
    get_gps_vehicle.short_description = 'ТЗ'

    def link_to_owner_name(self, obj):
        if obj.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html(
                    "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.gps.owner.id), str(obj.gps.owner.name)))
            else:
                return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник назва'

    def link_to_owner_login(self, obj):
        if obj.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html(
                    "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.gps.owner.id), str(obj.gps.owner.login)))
            else:
                return 'CKT'

    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Власник Login'


admin.site.register(FuelSensor, FuelSensorAdmin)
admin.site.register(Sim, SimAdmin)
admin.site.register(Gps, GpsAdmin)