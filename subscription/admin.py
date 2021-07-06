from django.contrib import admin
from .models import Subscription, Letters, Client
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
from rangefilter.filters import DateRangeFilter


class LettersAdmin(admin.ModelAdmin):
    raw_id_fields = ('client','gps')
    list_per_page = 20
    list_display = ('date_letter',
                    'get_link_client_name',
                    'get_link_client_login',
                    'get_link_gps',
                    'get_action',
                    'gps_rate',
                    'get_new_rate',
                    'status',
                    )
    list_filter = ('gps',
                   ('date_letter',DateRangeFilter),
                   'action',
                   'status',
                   'client__login',
                   )
    search_fields = [
                     'gps__number',
                     ]

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.client.id), str(obj.client.name)))

    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    def get_link_client_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.client.id), str(obj.client.login)))

    get_link_client_login.admin_order_field = 'client_login'
    get_link_client_login.short_description = 'Login'

    def get_link_gps(self, obj):
        return format_html(
            "<a href='../../products/gps/%s/change/' >%s</a>" % (
                str(obj.gps.id), str(obj.gps.number)))

    get_link_gps.admin_order_field = 'gps_number'
    get_link_gps.short_description = 'БР'

    def get_action(self, obj):
        return obj.get_action_display()

    get_action.admin_order_field = 'action'
    get_action.short_description = 'Дія'

    def get_new_rate(self, obj):
        return obj.get_new_rate_display()

    get_new_rate.admin_order_field = 'new_rate'
    get_new_rate.short_description = 'на тариф'


class SubscriptionAdmin(admin.ModelAdmin):
    raw_id_fields = ('client',)
    list_per_page = 20
    actions = ['update_activation', 'update_status_payment', 'update_all']

    def update_activation(self, request, queryset):
        for subscriptions in queryset:
            subscriptions.activation = True
            subscriptions.save()

    update_activation.short_description = "Нарахувати активацію"

    def update_status_payment(self, request,queryset):
        for subscriptions in queryset:
            subscriptions.status = 'Сплачено'
            subscriptions.save()

    update_status_payment.short_description = 'Встановити "Сплачено"'

    def update_all(self, request, queryset):
        for subscriptions in queryset:
            subscriptions.save()

    update_all.short_description = "Оновити дані з сьогоднішнього числа"

    list_filter = (
        'quarter',
        'client__login',
        'client__name',
        'client__provider',
        'status',
        'activation',
    )

    list_display = (
        'get_date_init',
        'get_quarter',
        'get_year',
        'get_link_client_name',
        'get_link_client_login',
        'get_provider',
        'price_quarter',
        'sum_payment',
        'get_link_invoice',
        'sum_to_pay',
        'status',
        'activation',
        'activation_sum',

        'price_1m',
        'price_2m',
        'price_3m',
        'all_1m',
        'all_2m',
        'all_3m',

        'rate_ua_1m',
        'rate_world_1m',
        'rate_pause_1m',
        'rate_own_sim_1m',

        'rate_ua_2m',
        'rate_world_2m',
        'rate_pause_2m',
        'rate_own_sim_2m',

        'rate_ua_3m',
        'rate_world_3m',
        'rate_pause_3m',
        'rate_own_sim_3m',

    )

    def get_link_invoice(self, obj):
        display_text = ", ".join([
            "<a href={}>{} \nна сумму {}грн\n</a>".format(
                reverse('admin:invoices_subinvoice_change', args=(sub_invoice.pk,)), str(sub_invoice), sub_invoice.invoice_sum,)
            for sub_invoice in obj.sub_invoice.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_invoice.short_description = 'Рах.фактура'
    get_link_invoice.allow_tags = True

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

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.client.id), str(obj.client.name)))

    get_link_client_name.admin_order_field = 'client_name'
    get_link_client_name.short_description = 'Платник'

    def get_link_client_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.client.id), str(obj.client.login)))

    get_link_client_login.admin_order_field = 'client'
    get_link_client_login.short_description = 'Login'

    def get_quarter(self, obj):
        return obj.get_quarter_display()

    get_quarter.admin_order_field = 'quarter'
    get_quarter.short_description = 'Квартал'


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Letters, LettersAdmin)

