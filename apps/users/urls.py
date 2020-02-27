from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileList.as_view(), name='user_profile_list'),
    path('<int:user_profile_id>/', views.UserProfileDetail.as_view(),
         name='user_profile'),

]
