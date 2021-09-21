from django.contrib import admin
from projects.models import Project
from invoices.models import ProjectInvoice
from contracts.models import Contract, Additions
from django.utils.html import format_html
from django.urls import reverse
from rangefilter.filters import DateRangeFilter


class ProjectAdmin(admin.ModelAdmin):
    list_per_page = 4
    list_filter = (
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
        'date_finish',
        'date_start',
        'get_link_client_name',
        'amount_gps',
        'amount_fuel_sensor',
        'get_amount_gps_wo',
        'get_amount_fuel_sensor_wo',
        'add_costs',
        'sum',
        'get_link_invoice',
        'get_link_salenvoice',
        'get_link_contract_addition',
        'get_contract_addition_status',
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

    def get_link_contract_addition(self, obj):
        if obj.contract_project_to:
            return format_html(
                "<a href='../../contracts/contract/%s/change/' >%s</a>" % (
                    str(obj.contract_project_to.id),
                    'Дог. №{} від {}'.format(obj.contract_project_to.number, obj.contract_project_to.contract_date, )))
        elif obj.addition:
            return format_html(
                "<a href='../../contracts/additions/%s/change/' >%s</a>" % (
                    str(obj.addition.id),
                    'ДУ №{} від {}'.format(obj.addition.number, obj.addition.contract_date, )))
        else:
            return '-'

    get_link_contract_addition.admin_order_field = 'contract'
    get_link_contract_addition.short_description = 'Договір'

    def get_contract_addition_status(self, obj):
        if obj.contract_project_to:
            return obj.contract_project_to.status
        elif obj.addition:
            return obj.addition.status
        else:
            return '-'

    get_contract_addition_status.short_description = 'Статус дог/ду'

    def get_link_invoice(self, obj):
        display_text = ", ".join([
            "<a href={}>{} {} {} {}грн.</a>".format(
                reverse('admin:invoices_projectinvoice_change', args=(project_invoice.pk,)), str(project_invoice),
                project_invoice.status_payment, project_invoice.date_payment, project_invoice.sum_payment,
            )
            for project_invoice in obj.project_invoice.all()
        ])
        if display_text:
            return format_html(display_text)
        return "-"

    get_link_invoice.admin_order_field = 'invoice'
    get_link_invoice.short_description = 'Рахунок Фактура/Kасовий Oрдер'

    def get_link_salenvoice(self, obj):
        display_text = []
        for project_invoice in obj.project_invoice.all():
            if project_invoice.saleinvoice:
                display_text.append(project_invoice.saleinvoice)
            return "-"
        display_text = ", ".join([
            "<a href={}>{} {} {} </a>".format(
                reverse('admin:invoices_saleinvoice_change', args=(project_invoice.saleinvoice.pk,)),
                str(project_invoice.saleinvoice),
                project_invoice.saleinvoice.status, project_invoice.saleinvoice.date_status,
            )
            for project_invoice in obj.project_invoice.all()
        ])
        return format_html(display_text)

    get_link_salenvoice.admin_order_field = 'saleinvoice'
    get_link_salenvoice.short_description = 'BH'

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
