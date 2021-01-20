from django.contrib import admin
from .models import Contract, ContractSupplementary


class ContractSupplementaryInline(admin.StackedInline):
    model = ContractSupplementary
    fields = ('number', 'date', 'status')
    readonly_fields = ('number', 'date', 'status')


class ContractSupplementaryAdmin(admin.ModelAdmin):
    list_display = (
        'contract_to',
        'number',
        'date',
        'get_client_name',
        'get_provider',
    )

    def get_provider(self, obj):
        return obj.contract_to.provider

    get_provider.admin_order_field = 'client_name'
    get_provider.short_description = 'Постачальник'

    def get_client_name(self, obj):
        return obj.contract_to.client.name

    get_client_name.admin_order_field = 'client_name'
    get_client_name.short_description = 'Покупець / абонент'


class ContractAdmin(admin.ModelAdmin):
    inlines = [ContractSupplementaryInline]
    list_display = (
        'get_client_name',
        'get_client_login',
        'form',
        'provider',
        'number',
        'contract_date',
        'status',
        'status_date',
        'contract_image',
        'get_supplementary',
    )

    def get_supplementary(self, obj):
        queryset = obj.supplementary.all()
        sup = [i for i in queryset]
        return sup

    get_supplementary.short_description = 'ДУ'

    def get_client_name(self, obj):
        return obj.client.name

    get_client_name.admin_order_field = 'client_name'  # Allows column order sorting
    get_client_name.short_description = 'Покупець / абонент'  # Renames column head

    def get_client_login(self, obj):
        return obj.client.login

    get_client_login.admin_order_field = 'client_login'  # Allows column order sorting
    get_client_login.short_description = 'Login'  # Renames column head

    list_filter = ('form', 'provider', 'client', 'status',)
    search_fields = ['client', 'number', 'provider', ]


admin.site.register(ContractSupplementary, ContractSupplementaryAdmin)
admin.site.register(Contract, ContractAdmin)
