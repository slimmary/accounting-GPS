from django.urls import path

from . import views

urlpatterns = [
    path('', views.InvoicesList.as_view(), name='invoices_list'),
    path('saleinvoices/', views.SaleInvoicesList.as_view(), name='saleinvoices_list'),
    path('saleinvoices/<int:saleinvoices_id>', views.SaleInvoiceDetail.as_view(), name='saleinvoices_detail'),
    path('serviceinvoices/', views.ServiceInvoicesList.as_view(), name='serviceinvoices_list'),
    path('serviceinvoices/<int:serviceinvoices_id>', views.ServiceInvoiceDetail.as_view(), name='serviceinvoices_detail'),
    path('subinvoices/', views.SubInvoicesList.as_view(), name='subinvoices_list'),
    path('subinvoices/<int:subinvoices_id>', views.SubInvoiceDetail.as_view(), name='subinvoices_detail'),
    path('projectinvoices/', views.ProjectInvoiceList.as_view(), name='projectinvoices_list'),
    path('projectinvoices/<int:projectinvoices_id>', views.ProjectInvoiceDetail.as_view(), name='projectinvoices_detail'),

]