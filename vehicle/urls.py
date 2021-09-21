from django.urls import path

from . import views

urlpatterns = [
    path('', views.VehicleList.as_view(), name='vehicles_list'),
    path('/<int:vehicle_id>', views.SubscriptionDetail.as_view(), name='vehicle_detail'),

]