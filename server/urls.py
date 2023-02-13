"""server URL Configuration

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
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from social.views import PostViewSet, ResponseViewSet
from social.user.views import UserViewSet
from social.auth.views import LoginViewSet, RegistrationViewSet, RefreshViewSet

from django.views.generic import TemplateView

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# post
routes.register(r'post', PostViewSet, basename='post')
routes.register(r'response', ResponseViewSet, basename='response')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(routes.urls)),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
