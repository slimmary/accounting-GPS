from django.contrib import admin
from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'lastname',
        'name',
        'position',
        'birthday',
        'day_start',
        'phone_1',
        'phone_2',
        'email_1',
        'email_2',
    )


admin.site.register(Staff, StaffAdmin)