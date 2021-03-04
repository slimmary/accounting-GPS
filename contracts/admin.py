from django.contrib import admin
from .models import Contract, Additions


class AdditionsInline(admin.TabularInline):
    model = Additions
    fields = ('number', 'contract_date', 'status')


class AdditionsAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'contract_date',
        'get_contract_to_provider',
        'get_contract_to',
        'get_client_name',
        'get_project',

    )

    def get_contract_to(self, obj):
        return '{} №{} від {} '.format(obj.contract_to.type, obj.contract_to.number, obj.contract_to.contract_date)

    get_contract_to.allow_tags = True
    get_contract_to.short_description = 'Договір до якого ДУ'

    def get_contract_to_provider(self, obj):
        return '{}'.format(obj.contract_to.provider)

    get_contract_to_provider.allow_tags = True
    get_contract_to_provider.short_description = 'Постачальник'

    def get_project(self, obj):
        if obj.contract_to.type == obj.contract_to.TypeChoice.project:
            return obj.contract_to.contract_project_to
        return '-'

    get_project.short_description = 'проект'

    def get_client_name(self, obj):
        return obj.contract_to.client.name

    get_client_name.admin_order_field = 'client_name'
    get_client_name.short_description = 'Покупець / абонент'


class ContractAdmin(admin.ModelAdmin):
    inlines = [AdditionsInline]
    list_display = (
        'get_client_name',
        'get_client_login',
        'type',
        'provider',
        'number',
        'contract_date',
        'status',
        'status_date',
        'contract_image',
        'get_additions',
        'get_project',
    )

    def get_project(self, obj):
        if obj.type == obj.TypeChoice.project:
            return obj.contract_project_to
        return '-'

    get_project.short_description = 'проект'

    def get_additions(self, obj):
        queryset = obj.additions.all()
        sup = [i for i in queryset]
        return sup

    get_additions.short_description = 'ДУ'

    def get_client_name(self, obj):
        return obj.client.name

    get_client_name.admin_order_field = 'client_name'  # Allows column order sorting
    get_client_name.short_description = 'Покупець / абонент'  # Renames column head

    def get_client_login(self, obj):
        return obj.client.login

    get_client_login.admin_order_field = 'client_login'  # Allows column order sorting
    get_client_login.short_description = 'Login'  # Renames column head

    list_filter = ('client', 'status', 'provider')
    search_fields = ['client', 'number', ]


admin.site.register(Contract, ContractAdmin)
admin.site.register(Additions, AdditionsAdmin)
