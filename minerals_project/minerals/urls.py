from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:mineral_id>/', views.mineral_detail, name='mineral_detail'),
    path('<int:mineral_id>/<str:section>/', views.datawrapper_redirect, name='datawrapper_redirect'),
]