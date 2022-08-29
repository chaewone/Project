from django.contrib import admin
from django.urls import path, include
from user.views import home

urlpatterns = [
    path('', home), # home 화면
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('product/', include("product.urls")),
]
