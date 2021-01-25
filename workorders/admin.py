from django.contrib import admin
from .models import CompletedWorks, WorkOrder
from django.utils.html import format_html


class CompletedWorksInline(admin.StackedInline):
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
        'milege_price_executor',
        'milege_price_client',
        'add_costs_executor',
        'add_costs_client',
        'description_add_costs',
        'month_executor_pay',
        'sum_price_client'
    )

    def get_link_project(self, obj):
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
