from django.contrib import admin
from .models import CompletedWorks, WorkOrder, ServicePlan, WorkOrderProxy, Expertise, ExecutorPayment, ExecutorPaymentProxy
from django.utils.html import format_html
from django.urls import reverse
from invoices.models import ProjectInvoice, Invoice
from rangefilter.filters import DateRangeFilter
from django.core.mail import send_mail


class ExpertiseAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'date_wo',
        'client',
        'gps',
        'fuel_sensor',
        'desription',
        'date_take_to_rapeir',
        'date_receving_expertise',
        'malfunctions',
        'result_expertise',
        'price_expertise',

    )

    list_filter = (
        'client',
        'client__login',
        ('date_wo', DateRangeFilter),
        ('date_take_to_rapeir', DateRangeFilter),
        ('date_receving_expertise',DateRangeFilter),
        'result_expertise',
        'price_expertise',
    )

    search_fields = [
        'gps__number',
        'fuel_sensor__number',
    ]


class InvoiceInline(admin.TabularInline):
    list_per_page = 20
    model = Invoice
    verbose_name_plural = 'РФ за сервісні роботи'


class ServicePlanAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_planing'
    list_per_page = 50
    list_display = (
        'date_create',
        'type_of_service',
        'get_distrit_or_city',
        'type_of_delivery',
        'tasks',
        'date_planing',
        'time',
        'client',
        'adress',
        'get_contacts',
        'respons_manager',
        'wo_numb',
        'date_ex',
        'executor',
        'status'
    )
    list_filter = (
        'status',
        'client',
        ('date_ex', DateRangeFilter),
    )

    def get_contacts(self, obj):
        if obj.contact_2:
            return obj.contact, obj.contact_2
        return obj.contact

    get_contacts.short_description = 'контакти'
    get_contacts.allow_tags = True

    def get_distrit_or_city(self, obj):
        if obj.city:
            return obj.city
        return obj.district

    get_distrit_or_city.short_description = 'регіон'

    actions = ['update_status', 'send_emails']

    def update_status(self, request, queryset):
        for works in queryset:
            works.status = works.StatusWOPlan.executed
            works.save()

    update_status.short_description = 'Виконано'

    def send_emails(self, request, queryset):
        for works in queryset:
            if works.district:
                city_district = works.district
            else:
                city_district = works.city
            send_mail(
                'ЗН №{} на {}'.format(works.wo_numb, works.date_ex),
                'Привіт, {}! тобі назначено на {} о {} год. за адресою: {} {} наступні роботи: {}'.format(
                    works.executor, works.date_ex, works.time, city_district, works.adress,works.tasks),
                'slimmarkelova@gmail.com',
                [works.executor.email,],
                fail_silently=False,
            )

    send_emails.short_description = 'Відправити e-mail виконавцю'


class CompletedWorksInline(admin.TabularInline):
    list_per_page = 5
    model = CompletedWorks
    verbose_name_plural = 'виконані роботи'


class CompletedWorksAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display_links = ('type_service',)
    list_display = (
        'get_work_order_date',
        'get_link_work_order',
        'type_service',
        'get_executor',
        'get_link_client',
        'get_link_vehicle',
        'get_link_gps',
        'get_link_fuelsensor',
        'get_used_equipment',
        'info',
        'payer',
    )

    list_filter = (
        'gps',
        'work_order__client',
        'work_order__executor',
        ('work_order__date',DateRangeFilter),
        'type_service',
    )
    search_fields = [
        'gps__number',
        'fuel_sensor__number',
        'work_order__number',
    ]

    def get_work_order_date(selfself, obj):
        return obj.work_order.date

    get_work_order_date.short_description = 'Дата'

    def get_link_work_order(self, obj):
        return format_html(
                "<a href='../../work_orders/work_order/%s/change/' >%s</a>" % (
                    str(obj.work_order.id), str(obj.work_order.number)))

    get_link_work_order.short_description = '№ ЗН'

    def get_link_fuelsensor(self, obj):
        if obj.fuel_sensor:
            return format_html(
                "<a href='../../products/fuelsensor/%s/change/' >%s</a>" % (
                    str(obj.fuel_sensor.id), str(obj.fuel_sensor)))
        return "-"

    get_link_fuelsensor.short_description = 'ДВРП'

    def get_link_gps(self, obj):
        if obj.gps:
            return format_html(
                "<a href='../../products/gps/%s/change/' >%s</a>" % (
                    str(obj.gps.id), str(obj.gps)))
        return "-"

    get_link_gps.short_description = 'БР'

    def get_link_vehicle(self, obj):
        return format_html(
            "<a href='../../vehicle/vehicle/%s/change/' >%s</a>" % (
                str(obj.car.id), str(obj.car)))

    get_link_vehicle.short_description = 'Транспортний засіб'

    def get_link_client(self, obj):
        return format_html(
            "<a href='../../clients/client/%s/change/' >%s</a>" % (
                str(obj.work_order.client.id), str(obj.work_order.client)))

    get_link_client.short_description = 'Клієнт'

    def get_executor(self, obj):
        return obj.work_order.executor

    get_executor.short_description = 'виконавець'

    def get_used_equipment(self, obj):
        list_equipment = []
        for equipments in obj.used_equipment.all():
            list_equipment.append(equipments)
        return list_equipment

    get_used_equipment.short_description = 'Використане обладнання'
    get_used_equipment.allow_tags = True


class WorkOrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    inlines = [CompletedWorksInline, InvoiceInline]
    list_per_page = 5
    list_filter = (
        ('date',DateRangeFilter),
        'type_of_work',
        'client',
        'client__login',
        'pay_form',
        'executor',
    )
    search_fields = [
        'number',
    ]

    list_display = (
        'number',
        'date',
        'type_of_work',
        'get_link_to_client',
        'get_link_project',
        'executor',
        'get_list_of_work',
        'get_list_of_equipment',
        'price_of_completed_works',
        'price_of_used_equipment',
        'pay_form',
        'milege',
        'milege_price_client',
        'add_costs_client',
        'description_add_costs',
        'sum_price_client',
        'get_link_invoices'
    )

    def get_link_to_client(self, obj):
        if obj.client:
            return format_html(
                "<a href='../../clients/client/%s/change/' >%s</a>" % (
                    str(obj.client.id), str(obj.client)))
        return "-"

    get_link_to_client.short_description = 'клієнт'

    def get_link_invoices(self, obj):
        if obj.type_of_work == obj.TypeWork.service:
            return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                'admin:invoices_invoice_change', args=(invoices.pk,)), str(invoices)) for invoices in obj.invoice_workorder.all()]))
        elif obj.type_of_work == obj.TypeWork.project:
            if obj.project:
                if obj.project.project_invoice:
                    return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
                        'admin:invoices_projectinvoice_change', args=(obj.project.project_invoice.pk,)), str(obj.project.project_invoice))]))
                return "-"
            return "-"
        return "-"

    get_link_invoices.short_description = 'РФ/KO'
    get_link_invoices.allow_tags = True

    def get_link_project(self, obj):
        if obj.project:
            return format_html(
                "<a href='../../projects/project/%s/change/' >%s</a>" % (str(obj.project.id), str(obj.project)))

    get_link_project.admin_order_field = 'workorder_project'
    get_link_project.short_description = 'Проект'

    def get_list_of_work(self, obj):
        result_dict = {}
        for work in obj.list_works.all():
            if work.type_service.name in result_dict:
                result_dict[work.type_service.name] += 1
            else:
                result_dict[work.type_service.name] = 1
        return '; '.join("{} - {}".format(k, v) for k, v in result_dict.items())

    get_list_of_work.allow_tags = True
    get_list_of_work.short_description = 'список виконаних робіт'

    def get_list_of_equipment(self, obj):
        equipment_dict = {}
        for work in obj.list_works.all():
            for equipment in work.used_equipment.all():
                if equipment.name in equipment_dict:
                    equipment_dict[equipment.name] += 1
                else:
                    equipment_dict[equipment.name] = 1
        return '; '.join("{} - {}".format(k, v) for k, v in equipment_dict.items())

    get_list_of_equipment.allow_tags = True
    get_list_of_equipment.short_description = 'використане обладнання'


class WorkOrderProxyAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_per_page = 20
    list_filter = (
        ('date',DateRangeFilter),
        'type_of_work',
        'client',
        'executor',
        ('month_executor_pay',DateRangeFilter),
    )

    list_display = (
        'number',
        'date',
        'get_month_year_executor_payment',
        'executor',
        'get_list_of_work',
        'milege',
        'milege_price_executor',
        'trip_day',
        'trip_day_costs_executor',
        'add_costs_executor',
        'description_add_costs',
    )

    def get_month_year_executor_payment(self,obj):
        if obj.month_executor_pay:
            return '{} {}р.'.format(obj.month_executor_pay.month,obj.month_executor_pay.year)
        return '-'

    get_month_year_executor_payment.short_description = 'місяць/рік ЗП'

    def get_list_of_work(self, obj):
        result_dict = {}
        for work in obj.list_works.all():
            if work.type_service.name in result_dict:
                result_dict[work.type_service.name] += 1
            else:
                result_dict[work.type_service.name] = 1
        return '; '.join("{} - {}".format(k, v) for k, v in result_dict.items())

    get_list_of_work.allow_tags = True
    get_list_of_work.short_description = 'список виконаних робіт'


class ExecutorPaymentAdmin(admin.ModelAdmin):
    date_hierarchy = 'period'
    list_per_page = 20
    list_display = [

        'get_period_month',
        'work_days_sum',
        'work_days_weekend_sum',
        'trip_day_sum',
        'qua_work_orders_sum',
        'qua_works_sum',
        'premium_sum',
        'boss_premium',
        

        'executor_1',
        'work_days_1',
        'work_days_weekend_1',
        'qua_work_orders_1',
        'qua_works_1',
        'trip_day_1',
        'trip_day_costs_1',
        'qua_payment_works_1',
        'milege_price_1',
        'premium_1',
        'total_payment_1',

        'executor_2',
        'work_days_2',
        'work_days_weekend_2',
        'qua_work_orders_2',
        'qua_works_2',
        'trip_day_2',
        'trip_day_costs_2',
        'milege_price_2',
        'premium_2',
        'total_payment_2',

        'qua_payment_works_2',
        'executor_3',
        'work_days_3',
        'work_days_weekend_3',
        'qua_work_orders_3',
        'qua_works_3',
        'trip_day_3',
        'trip_day_costs_3',
        'qua_payment_works_3',
        'milege_price_3',
        'premium_3',
        'total_payment_3',
    ]

    list_filter = (
        'executor_1',
        'executor_2',
        'executor_3',
    )

    def get_period_month(self,obj):
        return '{} / {}'.format(obj.period.month, obj.period.year,)

    get_period_month.short_description = 'місяць/рік ЗП'

    actions = ['update_status', ]

    def update_status(self, request, queryset):
        for executors in queryset:
            executors.save()

    update_status.short_description = 'Оновити дані'


class ExecutorPaymentProxyAdmin(admin.ModelAdmin):
    date_hierarchy = 'period'
    list_per_page = 20
    list_display = [

        'get_period_month',
        'qua_payment_works_sum',
        'premium_sum',
        'boss_premium',
        'get_executors_premium',

        'executor_1',
        'trip_day_costs_1',
        'qua_payment_works_1',
        'milege_price_1',
        'premium_1',
        'total_payment_1',

        'executor_2',
        'trip_day_costs_2',
        'milege_price_2',
        'premium_2',
        'total_payment_2',

        'qua_payment_works_2',
        'executor_3',
        'trip_day_costs_3',
        'qua_payment_works_3',
        'milege_price_3',
        'premium_3',
        'total_payment_3',
    ]

    list_filter = (
        'executor_1',
        'executor_2',
        'executor_3',
    )

    def get_executors_premium(self, obj):
        return obj.premium_sum - obj.boss_premium

    get_executors_premium.short_description = 'премія монтажників'

    def get_period_month(self, obj):
        return '{} / {}'.format(obj.period.month, obj.period.year, )

    get_period_month.short_description = 'місяць/рік ЗП'

    actions = ['update_status', ]

    def update_status(self, request, queryset):
        for executors in queryset:
            executors.save()

    update_status.short_description = 'Оновити дані'


admin.site.register(ExecutorPaymentProxy, ExecutorPaymentProxyAdmin)
admin.site.register(ExecutorPayment, ExecutorPaymentAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(WorkOrderProxy, WorkOrderProxyAdmin)
admin.site.register(CompletedWorks, CompletedWorksAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(ServicePlan, ServicePlanAdmin)
