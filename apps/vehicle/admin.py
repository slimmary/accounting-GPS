from django.contrib import admin
from .models import Vehicle


class ContractAdmin(admin.ModelAdmin):
    raw_id_fields = ("vehicle",)


admin.site.register(Vehicle)
