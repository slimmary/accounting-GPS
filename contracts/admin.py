from django.contrib import admin
from .models import Contract, Additions
from django.utils.html import format_html
from django.urls import reverse
from rangefilter.filters import DateRangeFilter


class AdditionsInline(admin.TabularInline):
    model = Additions
    fields = ('number', 'contract_date', 'status')


class AdditionsAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'contract_date',
        'get_contract_to_provider',
        'get_link_contract_to',
        'get_link_client',
        'get_link_project',

    )
    raw_id_fields = ('contract_to',)
    search_fields = [
        'number',
    ]
    list_filter = (
        'contract_to__client',
        'status',
        'contract_to__provider',
        ('contract_date',DateRangeFilter),
    )

    def get_link_project(self, obj):
        if obj.project_additions is not None:
            return format_html(
                "<a href='../../projects/project/%s/change/' >%s</a>" % (
                    str(obj.project_additions.id), str(obj.project_additions)))
        return '-'

    get_link_project.short_description = 'проект'

    def get_link_contract_to(self, obj):
        return format_html("<a href={}>№{} від {} \n</a>".format(
                reverse('admin:contracts_contract_change', args=(obj.contract_to.pk,)), obj.contract_to.number, obj.contract_to.contract_date)
                )

    get_link_contract_to.allow_tags = True
    get_link_contract_to.short_description = 'Договір до якого ДУ'

    def get_contract_to_provider(self, obj):
        return '{}'.format(obj.contract_to.provider)

    get_contract_to_provider.allow_tags = True
    get_contract_to_provider.short_description = 'Постачальник'

    def get_link_client(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.contract_to.client.id), str(obj.contract_to.client)))

    get_link_client.admin_order_field = 'client_name'
    get_link_client.short_description = 'Покупець / абонент'


class ContractAdmin(admin.ModelAdmin):
    inlines = [AdditionsInline]
    list_filter = (
        'client',
        'status',
        'provider',
        ('contract_date',DateRangeFilter),
    )
    search_fields = [
        'number',
    ]
    list_display = (
        'number',
        'get_link_client',
        'get_link_login',
        'type',
        'provider',
        'contract_date',
        'status',
        'status_date',
        'contract_image',
        'get_link_additions',
        'get_link_project',
    )

    def get_link_project(self, obj):
        if obj.type == obj.TypeChoice.project and obj.project_contract is not None :
            return format_html(
                "<a href='../../projects/project/%s/change/' >%s</a>" % (
                    str(obj.project_contract.id), str(obj.project_contract)))
        return '-'

    get_link_project.short_description = 'проект'

    def get_link_additions(self, obj):
        display_text = ", ".join([
            "<a href={}>{} \n</a>".format(
                reverse('admin:contracts_additions_change', args=(additions.pk,)), str(additions),
                )
            for additions in obj.additions.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_additions.allow_tags = True
    get_link_additions.short_description = 'ДУ'

    def get_link_client(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.client.id), str(obj.client.name)))

    get_link_client.admin_order_field = 'client_name'
    get_link_client.short_description = 'Покупець / абонент'

    def get_link_login(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (str(obj.client.id), str(obj.client.login)))

    get_link_login.admin_order_field = 'client_login'
    get_link_login.short_description = 'Login'


admin.site.register(Contract, ContractAdmin)
admin.site.register(Additions, AdditionsAdmin)
