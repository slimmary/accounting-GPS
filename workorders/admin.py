from django.contrib import admin
from .models import CompletedWorks, WorkOrder, ServicePlan
from django.utils.html import format_html


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

    def get_contacts(self,obj):
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
        'car',
        'type_service',
        'gps',
        'fuel_sensor',
        'get_used_equipment',
        'info',
        'payer',
    )

    def get_used_equipment(self, obj):
        return obj.used_equipment.all()

    get_used_equipment.short_description = 'Використане обладнання'


class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [CompletedWorksInline]
    list_per_page = 20
    list_display = (
        'date',
        'number',
        'type_of_work',
        'client',
        'get_link_project',
        'executor',
        # 'get_list_of_work',
        # 'list_of_used_equipment',
        'price_of_completed_works',
        'price_of_used_equipment',
        'pay_form',
        'milege',
        'milege_price_client',
        'add_costs_client',
        'description_add_costs',
        'sum_price_client'
    )

    def get_link_project(self, obj):
        if obj.project:
            return format_html("<a href='../../projects/project/%s/change/' >%s</a>" % (str(obj.project.id),str(obj.project)))

    get_link_project.admin_order_field = 'workorder_project'
    get_link_project.short_description = 'Проект'

    # def get_list_of_work(self, obj):
    #     list_work = []
    #     count_queryset = 0
    #     for services in obj.list_works.all().filter(name=obj.list_works.type_service.name):
    #         count_queryset = +1
    #         count_work = '{} - {}'.format(obj.list_works.type_service.name, count_queryset)
    #         list_work.append(count_work)
    #     return list_work
    #
    # get_list_of_work.short_description = 'список виконаних робіт'


admin.site.register(CompletedWorks, CompletedWorksAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(ServicePlan, ServicePlanAdmin)
