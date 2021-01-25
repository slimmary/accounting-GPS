from django.contrib import admin
from projects.models import Project
from django.utils.html import format_html


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
        'get_link_invoice',
        'get_link_contract_or_additions',
        'get_payment_status',
        'get_date_payment',
        'get_sum_payment',
        'date_receipt_contract',
        'date_receipt_sale_invoice',
        'execution_status',
        'notes'
    )

    def get_link_contract_or_additions(self, obj):
        if obj.contract is None:
            return format_html(
                "<a href='../../contracts/additions/%s/change/' >%s</a>" % (
                    str(obj.additions.id), 'ДУ №{} від {}'.format(obj.additions.number, obj.additions.date,)))
        else:
            return format_html(
                "<a href='../../contracts/contract/%s/change/' >%s</a>" % (
                    str(obj.contract.id), 'Договір №{} від {}'.format(obj.contract.number, obj.contract.contract_date)))

    get_link_contract_or_additions.allow_tags = True
    get_link_contract_or_additions.admin_order_field = 'contract_or_addition'
    get_link_contract_or_additions.short_description = 'Договір/ДУ'

    def get_link_invoice(self, obj):
        return format_html(
            "<a href='../../invoices/projectinvoicetaxfree/%s/change/' >%s</a>" % (
                str(obj.invoice.id), str(obj.invoice)))

    get_link_invoice.admin_order_field = 'invoice'
    get_link_invoice.short_description = 'Рахунок Фактура/Kасовий Oрдер'

    def get_payment_status(self, obj):
        return obj.invoice.status_payment

    get_payment_status.admin_order_field = 'payment_status'
    get_payment_status.short_description = 'Статус оплати'

    def get_date_payment(self, obj):
        return obj.invoice.date_payment

    get_date_payment.admin_order_field = 'date_payment'
    get_date_payment.short_description = 'Дата оплати'

    def get_sum_payment(self, obj):
        return obj.invoice.sum_payment

    get_sum_payment.admin_order_field = 'sum_payment'
    get_sum_payment.short_description = 'Сума оплати'


admin.site.register(Project, ProjectAdmin)
