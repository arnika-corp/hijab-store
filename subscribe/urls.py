from django.urls import path

from . import views


app_name = 'subscribe'
urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('success', views.success, name="success"),
    path('error', views.error, name="error"),
    path('unsubscribe', views.unsubscribe, name="unsubscribe"),
]