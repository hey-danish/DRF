"""drfapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView, TokenVerifyView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('bookstore/',include('bookstore.urls')),
    path('world/', include('world.urls')),
    path('touristmap/', include('touristmap.urls')),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('drf/', include('drf.urls')),
    path('', views.app_root)
]