from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    
]
