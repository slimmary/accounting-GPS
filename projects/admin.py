from django.contrib import admin
from projects.models import Project
from invoices.models import ProjectInvoice
from contracts.models import Contract, Additions
from django.utils.html import format_html
from django.urls import reverse


class ContractInline(admin.TabularInline):
    model = Contract
    fields = ('number', 'type', 'contract_date', 'client', 'status',)


class AdditionsInline(admin.TabularInline):
    model = Additions
    fields = ('number', 'contract_date', 'status', 'contract_to')


class ProjectInvoiceInline(admin.TabularInline):
    model = ProjectInvoice
    fields = ('number', 'date', 'invoice_sum', 'pay_form', 'status_payment', 'sum_payment', 'date_payment')


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContractInline, AdditionsInline, ProjectInvoiceInline]
    list_per_page = 4

    list_filter = ('date_receipt_contract',
                   'date_receipt_sale_invoice',
                   'client',
                   'client__login',
                   'execution_status',
                   'project_invoice__pay_form',
                   'project_invoice__status_payment',
                   'project_status',

                   )
    search_fields = [
        'work_orders__number',
        'client__name',
        'client__login',
        'project_invoice__number'
    ]
    list_display = (
        'number',
        'project_status',
        'date_start',
        'get_link_client_name',
        'amount_gps',
        'amount_fuel_sensor',
        'get_amount_gps_wo',
        'get_amount_fuel_sensor_wo',
        'add_costs',
        'sum',
        'get_link_invoice',
        'get_link_contract',
        'get_link_additions',
        'get_payment_status',
        'get_date_payment',
        'get_sum_payment',
        'date_receipt_contract',
        'date_receipt_sale_invoice',
        'execution_status',
        'get_link_work_orders',
        'notes'
    )

    def get_link_client_name(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.client.id), str(obj.client)))

    get_link_client_name.admin_order_field = 'client'
    get_link_client_name.short_description = 'Клієнт'

    def get_amount_gps_wo(self, obj):
        sum_amount_gps = 0
        for i in obj.work_orders.all():
            sum_amount_gps += i.amount_gps
            return sum_amount_gps

    get_amount_gps_wo.short_description = 'встановлено СКТ'

    def get_amount_fuel_sensor_wo(self, obj):
        sum_amount_fuel_sensor = 0
        for i in obj.work_orders.all():
            sum_amount_fuel_sensor += i.amount_fuel_sensor
        return sum_amount_fuel_sensor

    get_amount_fuel_sensor_wo.short_description = 'встановлено ДВРП'

    def get_link_contract(self, obj):

        return format_html(
            "<a href='../../contracts/contract/%s/change/' >%s</a>" % (
                str(obj.project_contract.id),
                'Дог. №{} від {}'.format(obj.project_contract.number, obj.project_contract.contract_date, )))

    get_link_contract.admin_order_field = 'contract'
    get_link_contract.short_description = 'Договір'

    def get_link_additions(self, obj):

        return format_html(
            "<a href='../../contracts/additions/%s/change/' >%s</a>" % (
                str(obj.project_add_contract.id),
                'ДУ №{} від {}'.format(obj.project_add_contract.number, obj.project_add_contract.contract_date, )))

    get_link_additions.admin_order_field = '_addition'
    get_link_additions.short_description = 'ДУ'

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

        display_text = ", ".join([
            "<a href={}>{} \nСКТ-{} ДВРП -{}\n</a>".format(
                reverse('admin:workorders_workorder_change', args=(work_orders.pk,)), str(work_orders),
                work_orders.amount_gps, work_orders.amount_fuel_sensor)
            for work_orders in obj.work_orders.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_work_orders.allow_tags = True
    get_link_work_orders.admin_order_field = 'work_orders'
    get_link_work_orders.short_description = 'Заказ-Наряди'


admin.site.register(Project, ProjectAdmin)
