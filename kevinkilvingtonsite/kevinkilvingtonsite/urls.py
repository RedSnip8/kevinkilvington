"""kevinkilvingtonsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from .sitemaps import AboutSitemap, AlbumsSitemap, EventsSitemap, HomeSitemap, PricesSitemap, StaticSitemap

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'about':AboutSitemap,
    'albums':AlbumsSitemap,
    'events':EventsSitemap,
    'prices':PricesSitemap,
    'index':HomeSitemap,
    'contact':StaticSitemap,
}

urlpatterns = [
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('prices/', include('prices.urls')),
    path('albums/',include('albums.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
