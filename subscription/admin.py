from django.contrib import admin
from django import forms
from .models import Subscription, Letters


class LettersAdmin(admin.ModelAdmin):
    list_per_page = 20
    readonly_fields = ['gps_rate', ]
    list_display = ('date',
                    'get_client_name',
                    'get_client_login',
                    'get_gps',
                    'get_action',
                    'gps_rate',
                    'get_new_rate',
                    )
    list_filter = ('gps',
                   'date',
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
    readonly_fields = [
        'rate_ua',
        'rate_world',
        'rate_ua_world',
        'rate_pause',
        'rate_own_sim',
        'price',
        'activation_sum',
    ]
    search_fields = [
        'get_client_name',
        'get_provider',
        'get_client_login',
    ]
    list_display = (
        'get_quarter',
        'get_year',
        'get_client_name',
        'get_client_login',
        'get_provider',
        'price',
        'get_all_gps',
        'rate_ua',
        'rate_world',
        'rate_ua_world',
        'rate_pause',
        'rate_own_sim',
        'status',
        'activation',
        'activation_sum',
    )

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

    def get_all_gps(self, obj):
        queryset = obj.client.gps.all().count()
        return queryset

    get_all_gps.admin_order_field = 'gps_all'
    get_all_gps.short_description = 'Кількість БР'


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Letters, LettersAdmin)
