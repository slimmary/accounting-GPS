from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContractList.as_view(), name='contract_list'),
    path('<int:contract_id>', views.ContractDetail.as_view(), name='contract_detail'),
]
