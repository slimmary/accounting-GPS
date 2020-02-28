from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    raw_id_fields = ("contracts",)


admin.site.register(Contract)
