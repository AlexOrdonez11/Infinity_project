from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_page, name="web_page"),
    path('update_item/', views.updateItem, name="update_item"),
    path('real_state/', views.processOrder, name="realstate"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout")
]