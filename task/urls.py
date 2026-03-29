from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.tasklist, name='tasklist'),
    path('create/', views.task_create, name='task_forms'),
    path('task/<int:task_id>/task_details', views.task_details, name='task_details'),
    path('task/<int:task_id>/delete', views.task_delete, name='task_delete'),
    path('task/<int:task_id>/task_mark_compeleted', views.task_mark_compeleted, name='task_mark_compeleted'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(), name= 'logout'),
]