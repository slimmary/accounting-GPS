from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='client_list'),
    path('<int:client_id>', views.ClientDetail.as_view(), name='client_detail'),

    path('address/', views.ClientPostAddressList.as_view(), name='post_address_list'),
    path('address/<int:client_id>', views.ClientPostAddressDetail.as_view(), name='post_address'),

    path('contact/', views.ContactProfileList.as_view(), name='contact_list'),
    path('contact/<int:client_id>', views.ContactProfileDetail.as_view(), name='contact_client'),


]
