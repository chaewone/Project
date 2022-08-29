from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]