from django.urls import path
from . import views

urlpatterns = [
    path('', views.mediciones_list, name='mediciones_list'),
]
