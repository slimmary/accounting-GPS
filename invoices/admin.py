from django.contrib import admin
from invoices.models import SubInvoice
from clients.models import Client
from django.db.models import Q


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
                return queryset.filter(client=None)
            elif self.value():
                return queryset.filter(Q(client_id=self.value()))
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
                return queryset.filter(client=None)
            elif self.value():
                return queryset.filter(Q(client_id=self.value()))
            else:
                return queryset

    list_per_page = 20
    list_display = ('provider',
                    'number',
                    'date',
                    'subscription',
                    'get_client_name',
                    'get_client_login',
                    'invoice_sum',
                    )
    list_filter = ('date',
                   'subscription',
                   LoginListFilter,
                   ClientNameListFilter,
                   )

    def get_client_name(self, obj):
        return obj.subscription.client.name

    get_client_name.admin_order_field = 'client'
    get_client_name.short_description = 'Клієнт'

    def get_client_login(self, obj):
        return obj.subscription.client.login

    get_client_login.admin_order_field = 'client_login'
    get_client_login.short_description = 'Login'


admin.site.register(SubInvoice, SubInvoiceAdmin)
