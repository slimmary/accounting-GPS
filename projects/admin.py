from django.contrib import admin
from projects.models import Project
from invoices.models import ProjectInvoice
from contracts.models import Contract, Additions
from django.utils.html import format_html
from django.urls import reverse


class ContractInline(admin.TabularInline):
    model = Contract
    fields = ('number', 'contract_date', 'client',)


class AdditionsInline(admin.TabularInline):
    model = Additions
    fields = ('number', 'contract_date', 'status', 'contract_to')


class ProjectInvoiceInline(admin.TabularInline):
    model = ProjectInvoice
    fields = ('number', 'date', 'invoice_sum', 'pay_form')


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContractInline, AdditionsInline, ProjectInvoiceInline]
    list_per_page = 20
    list_display = (
        'number',
        'project_status',
        'date_start',
        'client',
        'amount_gps',
        'amount_fuel_sensor',
        # 'get_amount_gps_wo',
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
        'get_link_work_orders',
        'notes'
    )

    # def get_amount_gps_wo(self, obj):
    #     sum_amount = 0
    #     for i in obj.work_orders.all():
    #         sum_amount += i.amount_gps
    #     return sum_amount
    #
    # get_amount_gps_wo.short_description = 'встановлено СКТ'

    def get_link_contract_or_additions(self, obj):
        if obj.project_contract:
            return format_html(
                "<a href='../../contracts/contract/%s/change/' >%s</a>" % (
                    str(obj.project_contract.id), 'Дог. №{} від {}'.format(obj.project_contract.number, obj.project_contract.contract_date,)))
        elif obj.project_add_contract:
            return format_html(
                "<a href='../../contracts/additions/%s/change/' >%s</a>" % (
                    str(obj.project_add_contract.id),
                    'ДУ №{} від {}'.format(obj.project_add_contract.number, obj.project_add_contract.contract_date, )))
        return '-'

    get_link_contract_or_additions.admin_order_field = 'contract_or_addition'
    get_link_contract_or_additions.short_description = 'Договір/ДУ'

    def get_link_invoice(self, obj):
        if obj.project_invoice:
            return format_html(
                "<a href='../../invoices/projectinvoice/%s/change/' >%s</a>" % (
                    str(obj.project_invoice.id), str(obj.project_invoice)))
        return '-'

    get_link_invoice.admin_order_field = 'invoice'
    get_link_invoice.short_description = 'Рахунок Фактура/Kасовий Oрдер'

    def get_payment_status(self, obj):
        if obj.project_invoice:
            return obj.project_invoice.status_payment
        return '-'

    get_payment_status.admin_order_field = 'payment_status'
    get_payment_status.short_description = 'Статус оплати'

    def get_date_payment(self, obj):
        if obj.project_invoice:
            return obj.project_invoice.date_payment
        return '-'

    get_date_payment.admin_order_field = 'date_payment'
    get_date_payment.short_description = 'Дата оплати'

    def get_sum_payment(self, obj):
        if obj.project_invoice:
            return obj.project_invoice.sum_payment
        return '-'

    get_sum_payment.admin_order_field = 'sum_payment'
    get_sum_payment.short_description = 'Сума оплати'

    def get_link_work_orders(self, obj):
        sum_amount_gps = 0
        sum_amount_fuel_sensor = 0
        for i in obj.work_orders.all():
            sum_amount_gps += i.amount_gps
            sum_amount_fuel_sensor += i.amount_fuel_sensor

        display_text = ", ".join([
            "<a href={}>{} \nСКТ-{} ДВРП -{}\n</a>".format(
                reverse('admin:workorders_workorder_change', args=(work_orders.pk,)), str(work_orders), sum_amount_gps, sum_amount_fuel_sensor )
            for work_orders in obj.work_orders.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_work_orders.allow_tags = True
    get_link_work_orders.admin_order_field = 'work_orders'
    get_link_work_orders.short_description = 'Заказ-Наряди'


admin.site.register(Project, ProjectAdmin)
