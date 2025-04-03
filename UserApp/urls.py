from django.urls import path
from UserApp import views

urlpatterns = [
    path("Home/", views.Home, name="Home"),
    path("Add_order/", views.Add_order, name="Add_order"),
    path("Save_order/", views.Save_order, name="Save_order"),
    path("View_orders/", views.View_orders, name="View_orders"),
    path("Update_order/<int:order_id>/", views.Update_order, name="Update_order"),
    path("Update_orderdetails/<int:order_id>/", views.Update_orderdetails, name="Update_orderdetails"),
    path("Delete_order/<int:order_id>/", views.Delete_order, name="Delete_order"),

    path("", views.Sign_in, name="Sign_in"),
    path("Sign_up/", views.Sign_up, name="Sign_up"),
    path('Save_signup/', views.Save_signup, name="Save_signup"),
    path('Signin_check/', views.Signin_check, name="Signin_check"),
    path('Log_out/', views.Log_out, name="Log_out"),
]
