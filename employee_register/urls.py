from django.urls import path
from . import views

urlpatterns = [

    #path('', views.home, name='blog-home'),
    path('list/', views.employee_list, name='emp-list'),
  path('', views.employee_form, name='emp_insert'),
    path('<int:id>/', views.employee_form, name='update_form'),
   path('delete/<int:id>/', views.employee_delete, name='emp-delete'),
    ]