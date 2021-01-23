from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'number',
        'project_status',
        'date_start',
        'client',
        'amount_gps',
        'amount_fuel_sensor',
        'add_costs',
        'sum',
        'get_invoice',
        'get_contract_or_additions',
        'payment_status',
        'date_payment',
        'sum_payment',
        'date_receipt_contract',
        'date_raceipt_sale_invoice',
        'execution_status',
        'notes'
    )

    def get_contract_or_additions(self, obj):
        if obj.contract is None:
            return obj.additions
        else:
            return obj.contract

    get_contract_or_additions.admin_order_field = 'contract_or_addition'
    get_contract_or_additions.short_description = 'Договір/ДУ'

    def get_invoice(self, obj):
        if obj.pay_form == obj.PayForm.taxfree:
            return obj.project_invoice_taxfree
        else:
            return obj.project_invoice

    get_invoice.admin_order_field = 'invoice'
    get_invoice.short_description = 'Рахунок Фактура/Kасовий Oрдер'


admin.site.register(Project, ProjectAdmin)