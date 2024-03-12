"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phone import views as v1
from laptop import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.index,name='index'),
    path('showphone/',v1.showphone,name='showphone'),
    path('details/<int:id>/',v1.details,name='details'),
    path('auth_login/',v1.auth_login,name='auth_login'),
    path('auth_register/',v1.auth_register,name='auth_register'),
    path('auth_logout/',v1.auth_logout,name='auth_logout'),
    path('checkout/<int:id>/',v1.checkout,name='checkout'),
    path('checkout2/<int:id>/',v2.checkout2,name='checkout2'),
    path('add_to_cart/<int:id>/',v1.add_to_cart,name='add_to_cart'),
    path('add_to_cart2/<int:id>/',v2.add_to_cart2,name='add_to_cart2'),
    path('showlaptop/',v2.showlaptop,name='showlaptop'),
    path('lapdetails/<int:id>/',v2.lapdetails,name='lapdetails'),
    path('buy_now/<int:id>/',v1.buy_now,name='buy_now'),
    
]
