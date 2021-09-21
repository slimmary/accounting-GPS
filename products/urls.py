from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products_list'),
    path('equipments', views.EquipmentList.as_view(), name='equipments_list'),
    path('equipments/<int:equipment_id>', views.EquipmentDetail.as_view(), name='equipment_detail'),
    path('services/', views.ServiceList.as_view(), name='service_list'),
    path('services/<int:service_id>', views.ServiceDetail.as_view(), name='service_detail'),
    path('sims/', views.SimList.as_view(), name='sims_list'),
    path('sims/<int:sim_id>', views.SimDetail.as_view(), name='sim_detail'),
    path('gpss/', views.GpsList.as_view(), name='gpss_list'),
    path('gpss/<int:gps_id>', views.GpsDetail.as_view(), name='gps_detail'),
    path('fuelsensors/', views.FuelSensorList.as_view(), name='fuelsensors_list'),
    path('fuelsensors/<int:fuelsensor_id>', views.FuelSensorDetail.as_view(), name='fuelsensor_detail'),

]