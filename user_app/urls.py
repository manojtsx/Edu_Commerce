from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_user_list, name='all-users'),  # /adminpanel/users/
    path('add/staff/', views.add_staff, name='add-staff'),   # /adminpanel/add/staff
]
