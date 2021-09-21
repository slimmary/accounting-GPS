from rest_framework import serializers
from .models import ServiceInvoice,  SubInvoice, ProjectInvoice, SaleInvoice
from django.utils.html import format_html


class SaleInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleInvoice
        fields = '__all__'


class SaleInvoiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleInvoice
        fields = ('number', 'date', 'invoice')


class ServiceInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInvoice
        fields = '__all__'


class ServiceInvoiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInvoice
        fields = ('number', 'date', 'invoice_sum', 'status_payment', 'servise_work_order', 'servise_work_order__client')


class SubInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubInvoice
        fields = '__all__'


class SubInvoiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubInvoice
        fields = ('number', 'date', 'invoice_sum', 'status_payment', 'client', 'subscription')


class ProjectInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInvoice
        fields = '__all__'


class ProjectInvoiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInvoice
        fields = ('number', 'date', 'invoice_sum', 'status_payment', 'client', 'project_to', 'pay_form')


class InvoicesLinkSerializer(serializers.Serializer):
    sale_invoice = format_html("<a href='../../invoices/saleinvoices/'>Видаткові Накладні до проектів</a>")
    service_invoices = format_html("<a href='../../invoices/serviceinvoices/'>рахунки на послуги</a>")
    sub_invoices = format_html("<a href='../../invoices/subinvoices/'>АП рахунки фактури</a>")
    project_invoices = format_html("<a href='../../invoices/projectinvoices/'>рахунки фактури та касові ордери проекти</a>")