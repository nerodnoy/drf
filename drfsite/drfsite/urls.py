"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from restaurants.views import *
from rest_framework import routers

# Заменяет все path для CRUD
# router = routers.SimpleRouter()

# Здесь добавим basename, если убрали queryset из View
# basename='restaurants'
# router.register(r'restaurants', RestaurantsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),

    # авторизация на основе сессии
    # добавляются 2 пути: drf-auth/login & drf-auth/logout
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/restaurants/', RestaurantsAPIList.as_view()),
    path('api/v1/restaurants/<int:pk>/', RestaurantsAPIUpdate.as_view()),
    path('api/v1/restaurants_delete/<int:pk>/', RestaurantsAPIDestroy.as_view()),

    # djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # JWT-Token
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
