from django.urls import path
from . import views

urlpatterns = [
    path('', views.VehicleList.as_view(), name='vehicle_list'),
    path('<int:vehicle_id>/', views.VehicleDetail.as_view(),
         name='vehicle'),

]
