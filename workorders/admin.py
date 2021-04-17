from django.contrib import admin
from .models import CompletedWorks, WorkOrder, ServicePlan
from django.utils.html import format_html
from invoices.models import ProjectInvoice, Invoice


class InvoiceInline(admin.TabularInline):
    list_per_page = 20
    model = Invoice
    verbose_name_plural = 'РФ засервісні роботи'


class ServicePlanAdmin(admin.ModelAdmin):
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


class CompletedWorksInline(admin.TabularInline):
    list_per_page = 20
    model = CompletedWorks
    verbose_name_plural = 'виконані роботи'


class CompletedWorksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'work_order',
        'get_executor',
        'get_client',
        'car',
        'type_service',
        'gps',
        'fuel_sensor',
        'get_used_equipment',
        'info',
        'payer',
    )

    def get_client(self, obj):
        return obj.work_order.client

    get_client.short_description = 'Клієнт'
    get_client.allow_tags = True

    def get_executor(self, obj):
        return obj.work_order.executor

    get_executor.short_description = 'виконавець'
    get_executor.allow_tags = True

    def get_used_equipment(self, obj):
        list_equipment = []
        for equipments in obj.used_equipment.all():
            list_equipment.append(equipments)
        return list_equipment

    get_used_equipment.short_description = 'Використане обладнання'
    get_used_equipment.allow_tags = True


class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [CompletedWorksInline, InvoiceInline]
    list_per_page = 20
    list_filter = (
        'date',
        'number',
        'type_of_work',
        'client',
        'pay_form',
    )
    list_display = (
        'date',
        'number',
        'type_of_work',
        'client',
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
        'get_invoices'
    )

    def get_invoices(self, obj):
        if obj.type_of_work == obj.TypeWork.service:
            invoices_list = []
            for invoices in obj.invoice_workorder.all():
                invoices_list.append(invoices)
                return "\n".join(invoices_list)
        elif obj.type_of_work == obj.TypeWork.project:
            if obj.project is None:
                return "-"
            return obj.project.project_invoice
        return "-"

    get_invoices.short_description = 'РФ/KO'
    get_invoices.allow_tags = True

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


admin.site.register(CompletedWorks, CompletedWorksAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(ServicePlan, ServicePlanAdmin)
