from django.contrib import admin
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = (
        'type',
        'make',
        'model',
        'number',
        'get_owner_name',
        'get_owner_login',
        'get_gps',
    )

    def get_owner_name(self, obj):
        return obj.owner.name
    get_owner_name.admin_order_field = 'owner_name'  # Allows column order sorting
    get_owner_name.short_description = 'Власник назва'  # Renames column head

    def get_owner_login(self, obj):
        return obj.owner.login
    get_owner_login.admin_order_field = 'owner_login'  # Allows column order sorting
    get_owner_login.short_description = 'Власник login'  # Renames column head

    def get_gps(self, obj):
        return obj.gps
    get_gps.short_description = 'БР'


admin.site.register(Vehicle, VehicleAdmin)
