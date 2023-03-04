"""Gnovel URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from gnovelapi.views import check_user, register_user, UserComicView, UserView, ReviewView, ComicView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'comics', ComicView, 'comic')
router.register(r'reviews', ReviewView, 'review')
router.register(r'user_comics', UserComicView, 'user_comic')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('user_comics/', UserComicView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='user_comics'),
    path('user_comics/<int:user>/<int:comic>/', UserComicView.as_view({
        'delete': 'destroy'
    }), name='user_comic'),
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
