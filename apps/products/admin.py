from django.contrib import admin

from .models import Sim, Gps


class SimInline(admin.StackedInline):
    model = Sim
    fields = ('operator',
              'number',
              'rate_client',
              'account_number',
              'date_receive',
              )


class GpsAdmin(admin.ModelAdmin):
    inlines = [SimInline]
    fields = ('number', 'vehicle',)
    list_display = (
        'number',
        'vehicle',
        'get_vehicle_owner_name',
        'get_vehicle_owner_login',
        'get_sim_numb',
        'get_sim_rate_client'
    )

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


class SimAdmin(admin.ModelAdmin):
    list_filter = ('operator','account_number','gps','rate_client','installer','date_given')
    search_fields = ['number', 'gps', 'phone_2', 'email', ]
    list_display = (
        'operator',
        'number',
        'account_number',
        'date_receive',
        'installer',
        'date_given',
        'rate_client',
        'gps',
        'get_gps_vehicle_client_login',
    )

    def get_gps_vehicle_client_login(self, obj):
        return obj.gps.vehicle.owner.login
    get_gps_vehicle_client_login.admin_order_field = 'owner'
    get_gps_vehicle_client_login.short_description = 'Login'


admin.site.register(Sim, SimAdmin)
admin.site.register(Gps, GpsAdmin)