"""Projeto_Bryan URL Configuration

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
from rest_framework import routers
from meuapp01.api import viewsets as produtoview
import meuapp01.views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()

route.register(r'api', produtoview.ProdutoViewSet, basename='meuapp01')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('produtos/', meuapp01.views.produtos_cadastrados),
    path('produtos_aut/', meuapp01.views.produtos_autenticados),
    path('login/', meuapp01.views.login)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
