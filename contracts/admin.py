from django.contrib import admin
from .models import Contract, Additions


class AdditionsInline(admin.StackedInline):
    model = Additions
    fields = ('number', 'date', 'status')


class AdditionsAdmin(admin.ModelAdmin):
    list_display = (
        'contract_to',
        'number',
        'date',
        'get_client_name',
        'get_project',

    )

    def get_project(self, obj):
        if obj.contract_to.type == obj.contract_to.TypeChoice.project:
            return obj.project_to_additions
        else:
            return None

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
            return obj.project_to_contract
        else:
            return None

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
