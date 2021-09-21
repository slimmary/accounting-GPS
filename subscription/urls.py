from django.urls import path

from . import views

urlpatterns = [
    path('', views.SubLettersList.as_view(), name='projects_list'),
    path('subscriptions/', views.SubscriptionList.as_view(), name='subscriptions_list'),
    path('subscriptions/<int:subscriptions_id>', views.SubscriptionDetail.as_view(), name='subscriptions_detail'),
    path('letters/', views.SubscriptionList.as_view(), name='letters_list'),
    path('letters/<int:letters_id>', views.SubscriptionDetail.as_view(), name='letters_detail'),

]