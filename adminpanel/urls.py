from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),           # /admin/
    path('dashboard/', views.admin_dashboard, name='admin-dashboard'),   # /admin/dashboard/
]
