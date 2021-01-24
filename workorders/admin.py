from django.contrib import admin
from .models import CompletedServiceWorks, CompletedProjectWorks, WorkOrder


class CompletedProjectWorksInline(admin.StackedInline):
    list_per_page = 20
    model = CompletedProjectWorks
    verbose_name_plural = 'проектні виконані роботи'


class CompletedProjectWorksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'work_order_project',
        'car',
        'type_service',
        'gps',
        'fuel_sensor',
    )


class CompletedServiceWorksInline(admin.StackedInline):
    list_per_page = 20
    model = CompletedProjectWorks
    verbose_name_plural = 'сервісні виконані роботи'


class CompletedServiceWorksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'work_order_service',
        'car',
        'type_service',
        'get_used_equipment',
        'gps',
        'fuel_sensor',
        'payer',
    )

    def get_used_equipment(self, obj):
        return obj.used_equipment.all()

    get_used_equipment.short_description = 'Використане обладнання'


class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [CompletedServiceWorksInline, CompletedProjectWorksInline]
    list_per_page = 20
    list_display = (
        'date',
        'number',
        'type_of_work',
        'client',
        'project',
        'executor',
        'get_list_of_work',
        # 'list_of_used_equipment',
        'price_of_completed_works',
        'price_of_used_equipment',
        'info',
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

    def get_list_of_work(self, obj):
        if obj.type_of_work == obj.TypeWork.project:
            return obj.list_project_works.all()
        else:
            return obj.list_service_works.all()

    get_list_of_work.short_description = 'список виконаних робіт'


admin.site.register(CompletedProjectWorks, CompletedProjectWorksAdmin)
admin.site.register(CompletedServiceWorks, CompletedServiceWorksAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
