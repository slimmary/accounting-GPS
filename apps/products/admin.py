from django.contrib import admin

from .models import Sim, Gps


class SimInline(admin.StackedInline):
    model = Sim
    fields = ('operator','number', )


class GpsAdmin(admin.ModelAdmin):
    inlines = [SimInline]
    ist_display = (
        'number',
        'vehicle',
    )


class SimAdmin(admin.ModelAdmin):
    list_display = (
        'operator',
        'number',
        'account_number',
        'date_receive',
        'installer',
        'date_given',
    )


admin.site.register(Sim, SimAdmin)
admin.site.register(Gps, GpsAdmin)