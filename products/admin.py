from django.contrib import admin
from .models import Sim, Gps, FuelSensor, Equipment, Service
from clients.models import Client
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Q
from rangefilter.filters import DateRangeFilter


class EquipmentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'name',
        'price_client_taxfree',
        'price_client_tax',
        'price_taxfree',
        'price_tax',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'name',
        'price_client_taxfree',
        'price_client_tax',
        'price_taxfree',
        'price_tax',
        'salary_installer'
    )


class GpsAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner','vehicle','sim_1','sim_2')
    list_per_page = 20
    actions = ['rate_client_pause']
    list_display = (
        'number',
        'get_link_gps_fuel',
        'get_link_vehicle',
        'link_to_owner_name',
        'link_to_owner_login',
        'get_link_sim',
        'rate_client',
    )

    list_filter = (
        'owner__name',
        'owner__login',
        'rate_client',
    )
    search_fields = [
        'number',
        'sim_1',
        'sim_2',
    ]

    def get_link_vehicle(self,obj):
        if obj.vehicle:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:vehicle_vehicle_change', args=(obj.vehicle.pk,)), str(obj.vehicle))]))

    get_link_vehicle.short_description = 'транспортний засіб'

    def get_link_sim(self, obj):
        list_sim = []
        if obj.sim_1:
            list_sim.append(obj.sim_1)
            if obj.sim_2:
                list_sim.append(obj.sim_2)
        else:
            if obj.sim_2:
                list_sim.append(obj.sim_2)
        return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:products_sim_change', args=(sim.pk,)), str(sim)) for sim in list_sim]))

    get_link_sim.allow_tags = True
    get_link_sim.short_description = 'сім'

    def rate_client_pause(self, request, queryset):
        for gps in queryset:
            gps.rate_client = gps.Rate.pause
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

    def get_link_gps_fuel(self, obj):
        display_text = ", ".join([
            "<a href={}>{} \n</a>".format(
                reverse('admin:products_fuelsensor_change', args=(fuel_sensor.id,)), str(fuel_sensor),
            ) for fuel_sensor in obj.fuel_sensor.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_gps_fuel.short_description = 'ДВРП'


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
                return queryset.filter(Q(gps_sim_1__owner=None) | Q(gps_sim_2__owner=None))
            elif self.value():
                return queryset.filter(Q(gps_sim_1__owner__id=self.value()) | Q(gps_sim_2__owner__id=self.value()))
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
                return queryset.filter(Q(gps_sim_1__owner=None) | Q(gps_sim_2__owner=None))
            elif self.value():
                return queryset.filter(Q(gps_sim_1__owner__id=self.value()) | Q(gps_sim_2__owner__id=self.value()))
            else:
                return queryset

    list_per_page = 20
    list_filter = (
        'operator',
        'account_number',
        'installer',
        ('date_given',DateRangeFilter),
        'gps_sim_1',
        'gps_sim_2',
        LoginListFilter,
        ClientNameListFilter,
    )
    search_fields = ['number', 'gps_sim_1__number', 'gps_sim_2__number',]
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
        if obj.gps_sim_1:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:products_gps_change', args=(gps.pk,)), gps.number) for gps in obj.gps_sim_1.all()]))
        elif obj.gps_sim_2:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:products_gps_change', args=(gps.pk,)), gps.number) for gps in obj.gps_sim_2.all()]))
        else:
            return 'CKT'

    link_to_gps.allow_tags = True
    link_to_gps.short_description = 'БР'

    def link_to_owner_name(self, obj):
        if obj.gps_sim_1:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:clients_client_change', args=(gps.owner.pk,)), gps.owner.name) for gps in obj.gps_sim_1.all()]))
        elif obj.gps_sim_2:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:clients_client_change', args=(gps.owner.pk,)), gps.owner.name) for gps in obj.gps_sim_2.all()]))
        else:
            return 'CKT'

    link_to_owner_name.allow_tags = True
    link_to_owner_name.short_description = 'Власник'

    def link_to_owner_login(self, obj):
        if obj.gps_sim_1:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:clients_client_change', args=(gps.owner.pk,)), gps.owner.login) for gps in obj.gps_sim_1.all()]))
        elif obj.gps_sim_2:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:clients_client_change', args=(gps.owner.pk,)), gps.owner.login) for gps in obj.gps_sim_2.all()]))
        else:
            return 'CKT'

    link_to_owner_login.allow_tags = True
    link_to_owner_login.short_description = 'Login'


class FuelSensorAdmin(admin.ModelAdmin):
    raw_id_fields = ('gps',)
    list_per_page = 20
    list_display = (
        'get_all_number',
        'type',
        'date_manufacturing',
        'get_link_gps_number',
        'get_link_gps_vehicle',
        'link_to_owner_name',
        'link_to_owner_login',
        'comments'
    )
    list_filter = (
        'type',
        ('date_manufacturing',DateRangeFilter),
        'gps',
        'gps__owner__name',
        'gps__owner__login',
    )
    search_fields = [
        'number',
        'gps__number',
    ]

    def get_all_number(self, obj):
        if obj.type == obj.Fuel_Type.cyfra:
            return 'D{}-{}'.format(obj.serial, obj.number)
        elif obj.type == obj.Fuel_Type.chastot:
            return 'H{}-{}'.format(obj.serial, obj.number)
        return '{}-{}'.format(obj.serial, obj.number)

    get_all_number.short_description = '№ ДВРП'

    def get_link_gps_number(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.id), str(obj.gps)))
        return '-'

    get_link_gps_number.admin_order_field = 'gps_number'
    get_link_gps_number.short_description = 'БР'

    def get_link_gps_vehicle(self, obj):
        if obj.gps.vehicle:
            return format_html(
                "<a href='../../vehicle/vehicle/%s/change/' >%s</a>" % (
                    str(obj.gps.vehicle.id), str(obj.gps.vehicle)))
        return '-'

    get_link_gps_vehicle.admin_order_field = 'gps_vehicle'
    get_link_gps_vehicle.short_description = 'ТЗ'

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
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Service, ServiceAdmin)
