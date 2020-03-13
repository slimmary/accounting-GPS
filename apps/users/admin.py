from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Профіль'
    fk_name = 'user'
    fields = ('avatar_tag','phone', 'phone_2','email', 'birthday', 'position')
    readonly_fields = ['avatar_tag']


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    list_display = (
        'avatar_tag',
        'get_last_login',
        'get_first_name',
        'get_last_name',
        'get_position',
        'get_birthday',
        'get_phone',
        'get_phone_2',
        'email',
        'get_email',

    )

    def avatar_tag(self, obj):
        return obj.profile.avatar_tag()
    avatar_tag.admin_order_field = 'avatar'
    avatar_tag.short_description = 'Фото'

    def get_last_login(self, obj):
        return obj.last_login
    get_last_login.admin_order_field = 'last_login'  # Allows column order sorting
    get_last_login.short_description = 'Останній раз online'  # Renames column head

    def get_first_name(self, obj):
        return obj.first_name
    get_first_name.admin_order_field = 'first_name'  # Allows column order sorting
    get_first_name.short_description = 'Прізвище'  # Renames column head

    def get_last_name(self, obj):
        return obj.last_name
    get_last_name.admin_order_field = 'last_name'  # Allows column order sorting
    get_last_name.short_description = "Ім'я"  # Renames column head

    def get_position(self, obj):
        return obj.profile.position
    get_position.admin_order_field = 'position'  # Allows column order sorting
    get_position.short_description = 'Посада'  # Renames column head

    def get_birthday(self, obj):
        return obj.profile.birthday
    get_birthday.admin_order_field = 'birthday'  # Allows column order sorting
    get_birthday.short_description = 'Дата народження'  # Renames column head

    def get_phone(self, obj):
        return obj.profile.phone
    get_phone.admin_order_field = 'phone'  # Allows column order sorting
    get_phone.short_description = 'Робочий телефон'  # Renames column head

    def get_phone_2(self, obj):
        return obj.profile.phone_2
    get_phone_2.admin_order_field = 'phone_2'  # Allows column order sorting
    get_phone_2.short_description = 'Власний телефон'  # Renames column head

    def get_email(self, obj):
        return obj.profile.email
    get_email.admin_order_field = 'email'  # Allows column order sorting
    get_email.short_description = 'Власний email'  # Renames column head


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
