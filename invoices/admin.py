from django.contrib import admin
from invoices.models import SubInvoice, ProjectInvoice, ProjectInvoiceTaxfree
from clients.models import Client
from django.db.models import Q
from django.utils.html import format_html


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
                    'project',
                    'client',
                    'invoice_sum',
                    )
    list_filter = ('date',
                   'project',
                   LoginListFilter,
                   ClientNameListFilter,
                   )


class ProjectInvoiceTaxfreeAdmin(admin.ModelAdmin):
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
    list_display = ('number',
                    'date',
                    'get_link_project',
                    'get_link_client_name',
                    'invoice_sum',
                    )

    def get_link_project(self, obj):
        return format_html(
            "<a href='../../projects/project/%s/change/' >%s</a>" % (
                str(obj.project.id), str(obj.project)))

    get_link_project.allow_tags = True
    get_link_project.admin_order_field = 'project'
    get_link_project.short_description = 'проект'

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.project.client.id), str(obj.project.client.name)))

    get_link_client_name.allow_tags = True
    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    list_filter = ('date',
                   'project',
                   LoginListFilter,
                   ClientNameListFilter,
                   )


admin.site.register(SubInvoice, SubInvoiceAdmin)
admin.site.register(ProjectInvoice, ProjectInvoiceAdmin)
admin.site.register(ProjectInvoiceTaxfree, ProjectInvoiceTaxfreeAdmin)
