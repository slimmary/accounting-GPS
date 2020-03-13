from django.contrib import admin
from .models import Contract, ContractSupplementary


class ContractSupplementaryInline(admin.StackedInline):
    model = ContractSupplementary
    fields = ('number', 'date')


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

    list_filter = ('form', 'provider', 'client', 'status', )
    search_fields = ['client', 'number', 'provider',]


admin.site.register(Contract, ContractAdmin)