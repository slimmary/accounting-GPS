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
        'payment_status',
        'date_payment',
        'sum_payment',
        'date_receipt_contract',
        'date_raceipt_sale_invoice',
        'execution_status',
        'notes'
    )

    def get_link_contract_or_additions(self, obj):
        if obj.contract is None:
            return format_html(
                "<a href='../../contracts/additions/%s/change/' >%s</a>" % (
                    str(obj.additions.id), str(obj.additions)))
        else:
            return format_html(
                "<a href='../../contracts/contract/%s/change/' >%s</a>" % (
                    str(obj.contract.id), str(obj.contract)))
    get_link_contract_or_additions.allow_tags = True
    get_link_contract_or_additions.admin_order_field = 'contract_or_addition'
    get_link_contract_or_additions.short_description = 'Договір/ДУ'

    def get_link_invoice(self, obj):
        if obj.pay_form == obj.PayForm.taxfree:
            return format_html(
                "<a href='../../invoices/projectinvoicetaxfree/%s/change/' >%s</a>" % (
                    str(obj.project_invoice_taxfree.id), str(obj.project_invoice_taxfree)))
        else:
            return format_html(
                "<a href='../../invoices/projectinvoice/%s/change/' >%s</a>" % (
                    str(obj.project_invoice.id), str(obj.project_invoice)))

    get_link_invoice.admin_order_field = 'invoice'
    get_link_invoice.short_description = 'Рахунок Фактура/Kасовий Oрдер'


admin.site.register(Project, ProjectAdmin)