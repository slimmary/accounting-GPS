from django.contrib import admin
from .models import Sim, Gps, FuelSensor


class SimInline(admin.StackedInline):
    list_per_page = 20
    model = Sim
    fields = ('operator',
              'number',
              'rate_client',
              'account_number',
              'date_receive',
              )


class GpsAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [SimInline]
    fields = ('number', 'vehicle',)
    list_display = (
        'number',
        'get_gps_fuel',
        'vehicle',
        'get_vehicle_owner_name',
        'get_vehicle_owner_login',
        'get_sim_numb',
        'get_sim_rate_client'
    )

    list_filter = (
        'number',
        'vehicle__owner__name',
        'vehicle__owner__login',
    )
    search_fields = [
        'number',
        'vehicle__owner__name',
        'vehicle__owner__login',
        'vehicle__number',
        'sim__number',
    ]

    def get_vehicle_owner_name(self, obj):
        return obj.vehicle.owner.name
    get_vehicle_owner_name.admin_order_field = 'vehicle_owner'
    get_vehicle_owner_name.short_description = 'Власник'

    def get_vehicle_owner_login(self, obj):
        return obj.vehicle.owner.login
    get_vehicle_owner_login.admin_order_field = 'vehicle_owner'
    get_vehicle_owner_login.short_description = 'Login'

    def get_sim_numb(self, obj):
        queryset = obj.sim.all()
        sim = [i.number for i in queryset]
        return sim
    get_sim_numb.short_description = 'Сім-Картки номер'

    def get_sim_rate_client(self, obj):
        queryset = obj.sim.all()
        sim = [i.get_rate_client_display() for i in queryset]
        return sim
    get_sim_rate_client.short_description = 'Сім-Картки Тариф'

    def get_gps_fuel(self, obj):
        queryset = obj.fuel_sensor.all()
        fuel = [i for i in queryset]
        return fuel
    get_gps_fuel.short_description = 'ДВРП'


class SimAdmin(admin.ModelAdmin):
    list_per_page = 20
    raw_id_fields = ('gps',)
    list_filter = ('operator','account_number','gps','rate_client','installer','date_given')
    search_fields = ['number',]
    list_display = (
        'get_operator',
        'number',
        'account_number',
        'date_receive',
        'installer',
        'date_given',
        'get_rate_client',
        'rate_price',
        'gps',
    )

    def get_operator(self, obj):
        return obj.get_operator_display()
    get_operator.admin_order_field = 'operator'
    get_operator.short_description = 'Оператор'

    def get_rate_client(self, obj):
        return obj.get_rate_client_display()
    get_rate_client.admin_order_field = 'rate_client'
    get_rate_client.short_description = 'Тариф'

    def get_gps_vehicle_client_login(self, obj):
        return obj.gps.vehicle.owner.login
    get_gps_vehicle_client_login.admin_order_field = 'owner'
    get_gps_vehicle_client_login.short_description = 'Login'


class FuelSensorAdmin(admin.ModelAdmin):
    list_per_page = 20
    fields = ('serial', 'number', 'date_manufacturing','gps')
    list_display = (
        'serial',
        'number',
        'date_manufacturing',
        'get_gps_number',
        'get_gps_vehicle',
        'get_gps_vehicle_owner_login',
        'get_gps_vehicle_owner_name',
    )
    list_filter = (
        'date_manufacturing',
        'gps',
        'gps__vehicle__owner__name',
        'gps__vehicle__owner__login',
    )
    search_fields = [
        'number',
        'gps__number',
        'gps__vehicle__owner__login',
    ]

    def get_gps_number(self, obj):
        return obj.gps.number
    get_gps_number.admin_order_field = 'gps_nubmer'
    get_gps_number.short_description = 'БР'

    def get_gps_vehicle(self, obj):
        return obj.gps.vehicle
    get_gps_vehicle.admin_order_field = 'vehicle'
    get_gps_vehicle.short_description = 'ТЗ'

    def get_gps_vehicle_owner_name(self, obj):
        return obj.gps.vehicle.owner.name
    get_gps_vehicle_owner_name.admin_order_field = 'vehicle_owner'
    get_gps_vehicle_owner_name.short_description = 'Власник'

    def get_gps_vehicle_owner_login(self, obj):
        return obj.gps.vehicle.owner.login
    get_gps_vehicle_owner_login.admin_order_field = 'vehicle_owner_login'
    get_gps_vehicle_owner_login.short_description = 'Login'


admin.site.register(FuelSensor, FuelSensorAdmin)
admin.site.register(Sim, SimAdmin)
admin.site.register(Gps, GpsAdmin)