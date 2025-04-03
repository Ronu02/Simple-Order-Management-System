from django.urls import path
from AdminApp import views

urlpatterns = [
    path("Dashboard/", views.Dashboard, name="Dashboard"),
    path("View_order/", views.View_order, name="View_order"),
    path("View_userdetails/", views.View_userdetails, name="View_userdetails"),

    path("Admin_login/", views.Admin_login, name="Admin_login"),
    path("Admin_loginCheck", views.Admin_loginCheck, name="Admin_loginCheck"),
    path('Admin_logout/', views.Admin_logout, name="Admin_logout"),
]
