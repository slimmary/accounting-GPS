from django.contrib import admin
from .models import Subscription, Letters


class LettersAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('date',
                    'get_client_name',
                    'get_client_login',
                    'get_gps',
                    'get_action',
                    'get_old_rate',
                    'get_new_rate',
                    )
    list_filter = ('gps',
                   'date',
                   'action',
                   'client__login',
                   'client__name'
                   )
    search_fields = ['get_client_name',
                     'get_client_login',
                     'get_action',
                     'get_gps'
                     ]

    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.admin_order_field = 'client'
    get_client_name.short_description = 'Клієнт'

    def get_client_login(self, obj):
        return obj.client.login
    get_client_login.admin_order_field = 'client_login'
    get_client_login.short_description = 'Login'

    def get_gps(self, obj):
        return obj.gps.number
    get_gps.admin_order_field = 'gps_number'
    get_gps.short_description = 'БР'

    def get_action(self, obj):
        return obj.get_action_display()
    get_action.admin_order_field = 'action'
    get_action.short_description = 'Дія'

    def get_old_rate(self, obj):
        return obj.get_old_rate_display()
    get_old_rate.admin_order_field = 'old_rate'
    get_old_rate.short_description = 'з тарифу'

    def get_new_rate(self, obj):
        return obj.get_new_rate_display()
    get_new_rate.admin_order_field = 'old_rate'
    get_new_rate.short_description = 'на тариф'


class SubscriptionAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = [
        'get_client_name',
        #'get_provider',
        'get_client_login',
    ]
    list_display = (
        'get_quarter',
        'get_year',
        'get_client_name',
        #'get_provider',
        'get_client_login',
        'get_all_gps',
        'get_rate_ukr',

    )

    #def get_provider(self, obj):
    #    return obj.get_provider_display()

    #get_provider.admin_order_field = 'provider'
    #get_provider.short_description = 'Постачальник (форма оплати)'

    def get_year(self, obj):
        return obj.year

    get_year.admin_order_field = 'year'
    get_year.short_description = 'Рік'

    def get_client_name(self, obj):
        return obj.client.name

    get_client_name.admin_order_field = 'client_name'
    get_client_name.short_description = 'Платник'

    def get_client_login(self, obj):
        return obj.client.login

    get_client_login.admin_order_field = 'client_login'
    get_client_login.short_description = 'Login'

    def get_quarter(self, obj):
        return obj.get_quarter_display()

    get_quarter.admin_order_field = 'quarter'
    get_quarter.short_description = 'Квартал'

    def get_all_gps(self, obj):
        queryset = obj.client.vehicle.all().count()
        return queryset

    get_all_gps.admin_order_field = 'gps_all'
    get_all_gps.short_description = 'Кількість БР'

    def get_rate_ukr(self, obj):
        queryset = obj.client.vehicle.all()
        gps = [i.gps for i in queryset]
        for a in gps:
            sim = a.sim.all()
            sim_rate = [b.get_rate_client_display() for b in sim]

            return sim_rate

    get_rate_ukr.short_description = 'Тарифи'


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Letters, LettersAdmin)
