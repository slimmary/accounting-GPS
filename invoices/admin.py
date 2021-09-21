from django.contrib import admin
from invoices.models import ServiceInvoice, SubInvoice, ProjectInvoice, SaleInvoice
from clients.models import Client
from django.db.models import Q
from django.utils.html import format_html
from datetime import date
from rangefilter.filters import DateRangeFilter
from django.urls import reverse


class ServiceInvoiceAdmin(admin.ModelAdmin):
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
                return queryset.filter(servise_work_order__client=None)
            elif self.value():
                return queryset.filter(Q(servise_work_order__client_id=self.value()))
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
                return queryset.filter(servise_work_order__client=None)
            elif self.value():
                return queryset.filter(Q(servise_work_order__client_id=self.value()))
            else:
                return queryset

    list_per_page = 20
    list_display = ('number',
                    'date',
                    'get_link_wo',
                    'get_link_client_name',
                    'get_link_client_login',
                    'invoice_sum',
                    'status_payment',
                    )
    list_filter = (
        ('date', DateRangeFilter),
        LoginListFilter,
        ClientNameListFilter,
        'status_payment',
    )

    search_fields = [
        'servise_work_order__number',
    ]

    def get_link_wo(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.servise_work_order.id), str(obj.servise_work_order)))

    get_link_wo.admin_order_field = 'wo'
    get_link_wo.short_description = 'ЗН'

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.servise_work_order.client.id), str(obj.servise_work_order.client.name)))

    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    def get_link_client_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.servise_work_order.client.id), str(obj.servise_work_order.client.login)))

    get_link_client_login.admin_order_field = 'client_login'
    get_link_client_login.short_description = 'Login'


class SubInvoiceAdmin(admin.ModelAdmin):
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
                return queryset.filter(subscription__client=None)
            elif self.value():
                return queryset.filter(Q(subscription__client_id=self.value()))
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
                return queryset.filter(subscription__client=None)
            elif self.value():
                return queryset.filter(Q(subscription__client_id=self.value()))
            else:
                return queryset

    list_per_page = 20
    list_display = ('provider',
                    'number',
                    'date',
                    'get_link_subscription',
                    'get_link_client_name',
                    'get_link_client_login',
                    'invoice_sum',
                    )
    search_fields = [
        'number',
    ]

    list_filter = (
        ('date', DateRangeFilter),
        'subscription',
        LoginListFilter,
        ClientNameListFilter,
    )

    def get_link_subscription(self, obj):
        return format_html(
            "<a href='../../subscription/subscription/%s/change/' >%s</a>" % (
                obj.subscription.id, str(obj.subscription)))

    get_link_subscription.admin_order_field = 'subscription'
    get_link_subscription.short_description = 'АП'

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                obj.subscription.client.id, str(obj.subscription.client.name)))

    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    def get_link_client_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                obj.subscription.client.id, str(obj.subscription.client.login)))

    get_link_client_login.admin_order_field = 'client_login'
    get_link_client_login.short_description = 'Login'


class ProjectInvoiceAdmin(admin.ModelAdmin):
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
                return queryset.filter(project__client=None)
            elif self.value():
                return queryset.filter(Q(project__client_id=self.value()))
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
                return queryset.filter(project__client=None)
            elif self.value():
                return queryset.filter(Q(project__client_id=self.value()))
            else:
                return queryset

        def get_link_saleinvoices(self, obj):
            return format_html(
                "<a href='../../invoices/saleinvoice/%s/change/' >%s</a>" % (
                    obj.saleinvoice.id, str(obj.saleinvoice)))

        get_link_saleinvoices.allow_tags = True
        get_link_saleinvoices.short_description = 'ВН'

    list_per_page = 20
    list_display = ('pay_form',
                    'number',
                    'date',
                    'get_link_client',
                    'get_link_project_invoice',
                    'invoice_sum',
                    'status_payment',
                    'sum_payment',
                    'date_payment',
                    'get_link_sale_invoices',
                    )
    list_filter = (LoginListFilter,
                   ClientNameListFilter,
                   ('date_payment', DateRangeFilter),
                   ('date', DateRangeFilter),
                   )
    search_fields = [
        'number',
    ]

    actions = ['update_status_payment']

    def update_status_payment(self, request, queryset):
        for projectinvoice in queryset:
            projectinvoice.sum_payment = projectinvoice.invoice_sum
            projectinvoice.status_payment = projectinvoice.Status_payment.paid
            projectinvoice.date_payment = date.today()
            projectinvoice.save()

    update_status_payment.short_description = "Сплачено"

    def get_link_project_invoice(self, obj):
        if obj.project:
            return format_html("<a href='../../projects/project/%s/change/' >%s</a>" % (str(obj.project.id),
                                                                                        str(obj.project)))

    get_link_project_invoice.allow_tags = True
    get_link_project_invoice.admin_order_field = 'project_to'
    get_link_project_invoice.short_description = 'Проект'

    def get_link_sale_invoices(self, obj):
        if obj.saleinvoice:
            return format_html("<a href='../../invoices/saleinvoice/%s/change/' >%s</a>" % (str(obj.saleinvoice.id),
                                                                                            str(obj.saleinvoice.number)))
        return '-'

    get_link_sale_invoices.allow_tags = True
    get_link_sale_invoices.admin_order_field = 'project_to'
    get_link_sale_invoices.short_description = 'Проект'

    def get_link_client(self, obj):
        if obj.project:
            return format_html(
                "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.project.client.id), str(obj.project.client.name)))

    get_link_project_invoice.allow_tags = True
    get_link_client.admin_order_field = 'client_invoice'
    get_link_client.short_description = 'Платник'


class SaleInvoiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('number',
                    'date',
                    'get_link_invoice',
                    'status',
                    'status_date'
                    )
    list_filter = (
        ('date', DateRangeFilter),
    )

    def get_link_invoice(self, obj):
        return format_html(
            "<a href='../../invoices/projectinvoice/%s/change/' >%s</a>" % (str(obj.invoice.id), str(obj.invoice)))

    get_link_invoice.allow_tags = True
    get_link_invoice.short_description = 'РФ'


admin.site.register(SaleInvoice, SaleInvoiceAdmin)
admin.site.register(ServiceInvoice, ServiceInvoiceAdmin)
admin.site.register(SubInvoice, SubInvoiceAdmin)
admin.site.register(ProjectInvoice, ProjectInvoiceAdmin)
