from django.contrib import admin
from .models import Subscription, Letters


class LettersAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('date_letter',
                    'get_client_name',
                    'get_client_login',
                    'get_gps',
                    'get_action',
                    'gps_rate',
                    'get_new_rate',
                    )
    list_filter = ('gps',
                   'date_letter',
                   'action',
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

    def get_new_rate(self, obj):
        return obj.get_new_rate_display()

    get_new_rate.admin_order_field = 'new_rate'
    get_new_rate.short_description = 'на тариф'


class SubscriptionAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = (
        'quarter',
        'client__login',
        'client__name',
        'status',
        'activation',
    )
    search_fields = [
        'get_client_name',
        'get_provider',
        'get_client_login',
    ]
    list_display = (
        'get_date_init',
        'get_quarter',
        'get_year',
        'get_client_name',
        'get_client_login',
        'get_provider',
        'price_quarter',
        'sum_payment',
        'sum_to_pay',
        'status',
        'activation_sum',

        'price_1m',
        'price_2m',
        'price_3m',
        'all_1m',
        'all_2m',
        'all_3m',

        'rate_ua_1m',
        'rate_world_1m',
        'rate_ua_world_1m',
        'rate_pause_1m',
        'rate_own_sim_1m',

        'rate_ua_2m',
        'rate_world_2m',
        'rate_ua_world_2m',
        'rate_pause_2m',
        'rate_own_sim_2m',

        'rate_ua_3m',
        'rate_world_3m',
        'rate_ua_world_3m',
        'rate_pause_3m',
        'rate_own_sim_3m',

    )

    def get_date_init(self, obj):
        return obj.date_init

    get_date_init.short_description = 'Дата створення'

    def get_provider(self, obj):
        return obj.client.provider

    get_provider.admin_order_field = 'provider'
    get_provider.short_description = 'Постачальник'

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


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Letters, LettersAdmin)
