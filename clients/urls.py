from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='clients_list'),
    path('<int:client_id>', views.ClientDetail.as_view(), name='client_detail'),

    path('contactprofile/', views.ContactProfileList.as_view(), name='contactprofile_list'),
    path('contactprofile/<int:contactprofile_id>', views.ContactProfileDetail.as_view(), name='contactprofile'),

    path('clientlegaldetail/', views.ClientLegalDetailList.as_view(), name='clientlegaldetail_list'),
    path('clientlegaldetail/<int:clientlegaldetail_id>', views.ClientLegalDetailDetail.as_view(), name='clientlegaldetail'),

    path('clientaddress/', views.ClientAddressList.as_view(), name='clientaddress_list'),
    path('clientaddress/<int:clientaddress_id>', views.ClientAddressDetail.as_view(), name='clientaddressdetail'),

]





