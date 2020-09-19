from django.contrib import admin
from .models import Sim, Gps, FuelSensor
from clients.models import Client
from django.utils.html import format_html


class GpsAdmin(admin.ModelAdmin):
    list_per_page = 20
    actions = ['rate_client_pause']
    list_display = (
        'number',
        'get_gps_fuel',
        'vehicle',
        'link_to_owner_name',
        'link_to_owner_login',

        'sim_1',
        'sim_2',
        'rate_client_1',
        'rate_client_2',
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
        'sim_1',
        'sim_2',
    ]

    def rate_client_pause(self, request, queryset):
        for gps in queryset:
            gps.rate_client_1 = gps.Rate.pause
            gps.rate_client_2 = gps.Rate.pause
            gps.save()

    rate_client_pause.short_description = 'Встановити тариф "Пауза"'

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

    class LoginListFilter(admin.SimpleListFilter):
        title = 'login власника'
        parameter_name = 'client_login'

        def lookups(self, request, model_admin):
            list_tuple = []
            for client in Client.objects.all():
                list_tuple.append((client.id, client.login.title()))
            list_tuple.append(('СКТ', 'СКТ'))
            return list_tuple

        def queryset(self, request, queryset):
            if self.value() == 'СКТ':
                return queryset.filter(gps_1__owner=None)
            elif self.value():
                return queryset.filter(gps_1__owner__id=self.value())
            else:
                return queryset

    class ClientNameListFilter(admin.SimpleListFilter):
        title = 'Назві власника'
        parameter_name = 'clients_name'

        def lookups(self, request, model_admin):
            list_tuple = []
            for client in Client.objects.all():
                list_tuple.append((client.id, client.name.title()))
            list_tuple.append(('СКТ', 'СКТ'))
            return list_tuple

        def queryset(self, request, queryset):
            if self.value() == 'СКТ':
                return queryset.filter(gps_1__owner=None)
            elif self.value():
                return queryset.filter(gps_1__owner__id=self.value())
            else:
                return queryset
            
    list_per_page = 20
    list_filter = (
        'operator',
        'account_number',
        'installer',
        'date_given',
        LoginListFilter,
        ClientNameListFilter,
    )
    search_fields = ['number', 'gps__number']
    list_display = (
        'operator',
        'number',
        'account_number',
        'date_receive',
        'installer',
        'date_given',
        'link_to_gps',
        'link_to_owner_name',
        'link_to_owner_login',
    )

    def link_to_gps(self, obj):
        if obj.gps_1 is None:
            if obj.gps_2 is None:
                return None
            else:
                return format_html("<a href='../../products/gps/%s/change/' >%s</a>" % (
                            str(obj.gps_2.id), str(obj.gps_2.number)))
        else:
            return format_html("<a href='../../products/gps/%s/change/' >%s</a>" % (
                            str(obj.gps_1.id), str(obj.gps_1.number)))

    link_to_gps.short_description = 'БР'

    def link_to_owner_name(self, obj):
        if obj.gps_1 is None:
            if obj.gps_2 is None:
                return 'CKT'
            else:
                if obj.gps_2 is not None:
                    if obj.gps_2.owner is None:
                        return 'CKT'
                    else:
                        return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (
                            str(obj.gps_2.owner.id), str(obj.gps_2.owner.name)))
        else:
            if obj.gps_1 is not None:
                if obj.gps_1.owner is None:
                    return 'CKT'
                else:
                    return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (
                        str(obj.gps_1.owner.id), str(obj.gps_1.owner.name)))
            else:
                return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник'

    def link_to_owner_login(self, obj):
        if obj.gps_1 is None:
            if obj.gps_2 is None:
                return 'CKT'
            else:
                if obj.gps_2 is not None:
                    if obj.gps_2.owner is None:
                        return 'CKT'
                    else:
                        return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (
                            str(obj.gps_2.owner.id), str(obj.gps_2.owner.login)))
        else:
            if obj.gps_1 is not None:
                if obj.gps_1.owner is None:
                    return 'CKT'
                else:
                    return format_html("<a href='../../clients/client/%s/change/' >%s</a>" % (
                        str(obj.gps_1.owner.id), str(obj.gps_1.owner.login)))
            else:
                return 'CKT'

    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Login'


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
        if obj.gps.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html(
                    "<a href='../../clients/client/%s/change/' >%s</a>" % (
                        str(obj.gps.owner.id), str(obj.gps.owner.name)))
            else:
                return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник'

    def link_to_owner_login(self, obj):
        if obj.gps.owner is None:
            return 'CKT'
        else:
            if obj.gps is not None:
                return format_html(
                    "<a href='../../clients/client/%s/change/' >%s</a>" % (
                        str(obj.gps.owner.id), str(obj.gps.owner.login)))
            else:
                return 'CKT'

    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Login'


admin.site.register(FuelSensor, FuelSensorAdmin)
admin.site.register(Sim, SimAdmin)
admin.site.register(Gps, GpsAdmin)
