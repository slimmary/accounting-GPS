from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('contracts/', include('contracts.urls')),
    path('invoices/', include('invoices.urls')),
    path('products/', include('products.urls')),
    path('projects/', include('projects.urls')),
    path('subscription/', include('subscription.urls')),
    path('vehicle/', include('vehicle.urls')),

    
]
