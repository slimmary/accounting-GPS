from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api-auth/', include('rest_framework.urls')),
    
    path('admin/', admin.site.urls),
    #path('auth/', include('apps.authenticate.urls')),
    path('clients/',include('apps.clients.urls')),
    path('users/',include('apps.users.urls')),
    path('contracts/',include('apps.contracts.urls')),
#    path('orders/',include('apps.orders.urls')),
#    path('products/',include('apps.products.urls')),
    path('users/',include('apps.users.urls')),
    path('vehicle/',include('apps.vehicle.urls')),
]
