from django.contrib import admin
from contracts.models import Contract
from .models import Client, ClientAddress, ContactProfile, ClientLegalDetail
from products.models import Gps
from django.utils.html import format_html


class ContactInline(admin.TabularInline):
    model = Client.contacts.through
    verbose_name_plural = "контактні особи < --- > клієнти"


class ClientLegalDetailInline(admin.StackedInline):
    list_per_page = 20
    model = ClientLegalDetail
    verbose_name_plural = 'Реквізити'


class GpsInline(admin.StackedInline):
    list_per_page = 20
    model = Gps
    fields = ('number', 'vehicle', 'rate_client_1', 'rate_client_2', 'rate_price')


class ContractInline(admin.StackedInline):
    list_per_page = 20
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [ContractInline, GpsInline, ClientLegalDetailInline, ContactInline, ]
    exclude = ('contacts', )
    list_display = (
        'name',
        'login',
        'edrpou',
        'status',
        'get_all_gps',
        'provider',
        'type_notification_1',
        'get_phone_email_contact_1',
        'type_notification_2',
        'get_phone_email_contact_2',
        'get_contacts',
    )

    list_filter = ('type_notification_2', 'type_notification_1', 'status', 'name', 'login',)
    search_fields = ['name', 'login', 'edrpou', 'login' ]

    def get_all_gps(self, obj):
        queryset = obj.gps.all().count()
        return queryset

    get_all_gps.admin_order_field = 'gps_all'
    get_all_gps.short_description = 'Кіл-ть БР'

    def get_phone_email_contact_1(self, obj):
        if obj.notification_contact_1 is not None:
            if obj.type_notification_1 == obj.Notification.email:
                return obj.notification_contact_1.email
            elif obj.type_notification_1 == obj.Notification.medoc:
                return '-'
            else:
                return obj.notification_contact_1.phone
        else:
            return '-'

    get_phone_email_contact_1.short_description = "телефон/адреса"

    def get_phone_email_contact_2(self, obj):
        if obj.notification_contact_2 is not None:
            if obj.type_notification_2 == obj.Notification.email:
                return obj.notification_contact_2.email
            elif obj.type_notification_2 == obj.Notification.medoc:
                return '-'
            else:
                return obj.notification_contact_2.phone
        else:
            return '-'

    get_phone_email_contact_2.short_description = "телефон/адреса"

    def get_contacts(self, obj):
        contacts_list = '|__________________________________________________________________________________________|' \
            .join([str(i) for i in obj.contacts.all()])
        return contacts_list

    get_contacts.short_description = "Контакти, з якими пов'язаний клієнт"
    get_contacts.admin_ordering_field = 'get_contacts'
    get_contacts.allow_tags = True


class ClientAddressAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('get_clients', 'index', 'region', 'district', 'city', 'street', 'house', 'office',)
    search_fields = ['get_clients', 'index', 'city', 'region', 'street', ]

    def get_clients(self, obj):
        if obj.client_legal_address.client is None:
            return obj.client_post_address.client
        else:
            return obj.client_legal_address.client

    get_clients.short_description = "Клієнти, з якими пов'язаний контакт"


class ContactProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]
    list_per_page = 20
    list_display_links = ['get_clients', 'firstname', 'surname', 'patronymic', ]
    list_display = ('get_clients', 'firstname', 'surname', 'patronymic', 'position', 'phone', 'phone_2', 'email',)
    list_filter = ('client_field',)
    search_fields = ['firstname', 'phone', 'phone_2', 'email', ]

    def get_clients(self, obj):
        clients = []
        for i in obj.client_field.all():
            clients.append(i)
        return clients

    get_clients.short_description = "Клієнти, з якими пов'язаний контакт"
    get_clients.allow_tags = True


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientAddress, ClientAddressAdmin)
admin.site.register(ContactProfile, ContactProfileAdmin)
