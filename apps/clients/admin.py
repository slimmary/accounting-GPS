from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    raw_id_fields = ("client",)


admin.site.register(Client)
