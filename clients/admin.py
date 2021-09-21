from django.contrib import admin
from contracts.models import Contract
from .models import Client, ClientAddress, ContactProfile, ClientProxyPayment, ClientLegalDetail, Provider
from vehicle.models import Vehicle
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django.db.models import Q
from jet.admin import CompactInline


class ContactInline(CompactInline):
    model = Client.contacts.through
    verbose_name_plural = "контактні особи < --- > клієнти"
    show_change_link = True


class VehicleInline(admin.StackedInline):
    list_per_page = 20
    model = Vehicle
    fields = ('number', 'rate_client', 'rate_price',)


class ContractInline(admin.StackedInline):
    list_per_page = 20
    model = Contract


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [ContractInline, VehicleInline, ]
    raw_id_fields = ['contacts', 'notification_contact_1', 'notification_contact_2']
    list_display = (
        'name',
        'login',
        'edrpou',
        'status',
        'get_all_gps',
        'provider',
        'legal_info',
        'type_notification_1',
        'get_phone_email_contact_1',
        'type_notification_2',
        'get_phone_email_contact_2',
        'get_contacts',
    )
    list_filter = ('type_notification_2', 'type_notification_1', 'status', 'name', 'login',)
    search_fields = ['name', 'login', 'edrpou', 'login']

    def get_all_gps(self, obj):
        queryset = obj.vehicle.all().count()
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
    inlines = [ContactInline, ]
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


class ClientProxyAdmin(admin.ModelAdmin):
    inlines = [ContractInline, VehicleInline, ContactInline, ]
    list_per_page = 20
    list_filter = ('name',
                   'login'
                   )
    list_display = (
        'name',
        'login',
        'get_gps_active',
        'get_gps_pause',
        'get_to_letters',
        'get_non_payed_invoices',
        'get_non_contracts',
        'get_to_wo_plan',
        'get_to_projects',
    )

    def get_gps_active(self, obj):
        count = 0
        for vehicle in obj.vehicle.all():
            if vehicle.rate_client != vehicle.Rate.pause:
                count = + 1
        url = (
                reverse("admin:vehicle_vehicle_changelist")
                + "?"
                + urlencode({"owner__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} </a>', url, count)

    get_gps_active.short_description = 'активні бр'

    def get_gps_pause(self, obj):
        count = 0
        for vehicle in obj.vehicle.all():
            if vehicle.rate_client == vehicle.Rate.pause:
                count = + 1
        url = (
                reverse("admin:vehicle_vehicle_changelist")
                + "?"
                + urlencode({"owner__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} </a>', url, count)

    get_gps_pause.short_description = 'пауза бр'

    def get_to_projects(self, obj):
        display_text = ",----------".join([
            "<a href={}>{}\n</a>".format(
                reverse('admin:projects_project_change', args=(project.pk,)), project, )
            for project in obj.project.all().filter(project_status='НЕ завершено')])
        return format_html(display_text)

    get_to_projects.short_description = 'НЕ завершені проекти'

    def get_to_wo_plan(self, obj):
        display_text = ",----------".join([
            "<a href={}>{}\n</a>".format(
                reverse('admin:workorders_serviceplan_change', args=(work_orders_plan.pk,)), work_orders_plan, )
            for work_orders_plan in obj.work_orders_plan.all().filter(status=None)])
        return format_html(display_text)

    get_to_wo_plan.short_description = 'заплановані роботи'

    def get_to_letters(self, obj):
        count = obj.letters.count()
        url = (
                reverse("admin:subscription_letters_changelist")
                + "?"
                + urlencode({"client__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} звернень </a>', url, count)

    get_to_letters.short_description = "звернення"
    get_to_letters.allow_tags = True

    def get_non_contracts(self, obj):
        contacts_result = []
        additions_result = []
        for cont in obj.contracts_all.all().filter(
                Q(status='Створений') | Q(status='Відправлений укрпоштою') |
                Q(status='Відправлений НП') | Q(status='Відправлений на електронну пошту')):
            contacts_result.append(cont)
        display_text_1 = ",".join([
            "<a href={}>Дог.№{} від {} {} з {} {} ---------\n</a>".format(
                reverse('admin:contracts_contract_change', args=(cont.pk,)), cont.number,
                cont.contract_date, cont.type, cont.provider, cont.status, )
            for cont in contacts_result])
        for cont in obj.contracts_all.all():
            for add in cont.additions.all().filter(
                    Q(status='Створений') | Q(status='Відправлений укрпоштою') |
                    Q(status='Відправлений НП') | Q(status='Відправлений на електронну пошту')):
                additions_result.append(add)
        display_text_2 = ",".join([
            "<a href={}>ДУ №{} від {} до Дог.№{}від {} {} з {} {} ----------\n</a>".format(
                reverse('admin:contracts_additions_change', args=(add.pk,)), add.number,
                add.contract_date, add.contract_to.number, add.contract_to.contract_date, add.contract_to,
                add.contract_to.provider, add.status, )
            for add in additions_result])

        if display_text_1 or display_text_2:
            return format_html(display_text_1 + display_text_2)
        return '-'

    get_non_contracts.short_description = "Дог./ДУ немає наявності"
    get_non_contracts.allow_tags = True

    def get_non_payed_invoices(self, obj):
        # result_list_1 = []
        result_list_2 = []
        result_list_3 = []
        # for wo in obj.work_orders.all():
        #     for inv in wo.invoice_workorder.all().filter(
        #             Q(status_payment='НЕ сплачено') | Q(status_payment='Частково сплачено')):
        #         result_list_1.append(inv)
        # display_text_1 = ",".join([
        #     "<a href={}> №{} від {} на {}грн. за ремонтні роботи {} ----------\n</a>".format(
        #         reverse('admin:invoices_invoice_change', args=(inv.pk,)), inv.number, inv.date, inv.invoice_sum,
        #         inv.status_payment, )
        #     for inv in result_list_1])

        for projects in obj.project.all():
            for invoices in projects.project_invoice.filter(
                    Q(status_payment='НЕ сплачено') | Q(status_payment='Частково сплачено')):
                result_list_2.append(invoices)
        display_text_2 = ",".join([
            "<a href={}> №{} від {} на {}грн. за придбання обладнання {} ---------\n</a>".format(
                reverse('admin:invoices_projectinvoice_change', args=(invoices.pk,)), invoices.number, invoices.date,
                invoices.invoice_sum,
                invoices.status_payment, )
            for invoices in result_list_2])

        for sub in obj.subscription.all():
            for sub_inv in sub.sub_invoice.all().filter(
                    Q(status_payment='НЕ сплачено') | Q(status_payment='Частково сплачено')):
                result_list_3.append(sub_inv)
        display_text_3 = ",".join([
            "<a href={}> №{} від {} на {}грн. за абонентське обслуговування {} ----------\n</a>".format(
                reverse('admin:invoices_subinvoice_change', args=(sub_inv.pk,)), sub_inv.number, sub_inv.date,
                sub_inv.invoice_sum,
                sub_inv.status_payment, )
            for sub_inv in result_list_3])
        # if display_text_1 or display_text_2 or display_text_3:
        if display_text_2 or display_text_3:
            # return format_html(display_text_1 + display_text_2 + display_text_3)
            return format_html(display_text_2 + display_text_3)
        return '-'

    get_non_payed_invoices.short_description = "не сплачені РФ"
    get_non_payed_invoices.allow_tags = True


class ClientLegalDetailAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['IPN', 'get_link_client', 'director', 'IBAN', 'bank_account', 'MFO', 'legal_address',
                    'post_address']
    search_fields = ['client', 'IPN', ]

    def get_link_client(self, obj):
        return format_html("<a href={}> {} {}</a>".format(reverse(
            'admin:clients_clientlegaldetai_change', args=obj.client_legal_detail.pk),
            obj.client_legal_detail.name, obj.client_legal_detail.login))

    get_link_client.short_description = 'клієнт'


class ProviderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'tax_type']


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientProxyPayment, ClientProxyAdmin)
admin.site.register(ClientAddress, ClientAddressAdmin)
admin.site.register(ContactProfile, ContactProfileAdmin)
admin.site.register(ClientLegalDetail, ClientLegalDetailAdmin)
admin.site.register(Provider, ProviderAdmin)
