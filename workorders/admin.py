from django.contrib import admin
from .models import CompletedServiceWorks


class CompletedServiceWorksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
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


admin.site.register(CompletedServiceWorks, CompletedServiceWorksAdmin)
