from django.contrib import admin
from invoices.models import SubInvoice, ProjectInvoice, Invoice
from clients.models import Client
from django.db.models import Q
from django.utils.html import format_html
from datetime import date
from rangefilter.filters import DateRangeFilter


class InvoiceAdmin(admin.ModelAdmin):
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
                return queryset.filter(wo__client=None)
            elif self.value():
                return queryset.filter(Q(wo__client_id=self.value()))
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
                return queryset.filter(wo__client=None)
            elif self.value():
                return queryset.filter(Q(wo__client_id=self.value()))
            else:
                return queryset
    raw_id_fields = ('wo',)
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
        'wo__number',
    ]

    def get_link_wo(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.wo.id), str(obj.wo)))

    get_link_wo.admin_order_field = 'wo'
    get_link_wo.short_description = 'ЗН'

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.wo.client.id), str(obj.wo.client.name)))

    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    def get_link_client_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.wo.client.id), str(obj.wo.client.login)))

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
    raw_id_fields = ('subscription',)
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
                return queryset.filter(project_to__client=None)
            elif self.value():
                return queryset.filter(Q(project_to__client_id=self.value()))
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
                return queryset.filter(project_to__client=None)
            elif self.value():
                return queryset.filter(Q(project_to__client_id=self.value()))
            else:
                return queryset
    raw_id_fields = ('project_to','client',)
    list_per_page = 20
    list_display = ('number',
                    'date',
                    'get_link_client',
                    'get_link_project_invoice',
                    'invoice_sum',
                    'status_payment',
                    'sum_payment',
                    'date_payment'
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
            projectinvoice.status_payment = projectinvoice.Status_payment.paid
            projectinvoice.date_payment = date.today()
            projectinvoice.save()

    update_status_payment.short_description = "Сплачено"

    def get_link_project_invoice(self, obj):
        return format_html("<a href='../../projects/project/%s/change/' >%s</a>" % (str(obj.project_to.id),
                                                                                    str(obj.project_to)))

    get_link_project_invoice.allow_tags = True
    get_link_project_invoice.admin_order_field = 'project_to'
    get_link_project_invoice.short_description = 'Проект'

    def get_link_client(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.client.id), str(obj.client.name)))

    get_link_project_invoice.allow_tags = True
    get_link_client.admin_order_field = 'client_invoice'
    get_link_client.short_description = 'Платник'


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(SubInvoice, SubInvoiceAdmin)
admin.site.register(ProjectInvoice, ProjectInvoiceAdmin)
