from django.contrib import admin
from .models import CompletedWorks, WorkOrder


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
        list_work = []
        for i in obj.list_works.all():
            list_work.append(i.type_service)
        return list_work

    get_list_of_work.short_description = 'список виконаних робіт'


admin.site.register(CompletedWorks, CompletedWorksAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
