from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.urls import reverse

from about.models import Photographer
from albums.models import Album, Events
from prices.models import Services
from home.models import Picture

class AboutSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    location = 'about/'

    def items(self):
        return Photographer.objects.filter(is_active=True)

class AlbumsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    location = 'albums/'

    def items(self):
        return Album.objects.filter(is_active=True)

class EventsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    location = 'albums/'

    def items(self):
        return Events.objects.filter(is_active=True)


class PricesSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1
    location = 'prices/'

    def items(self):
        return Services.objects.filter(is_availible=True)

class HomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    location = 'home/'

    def items(self):
        return Picture.objects.filter(on_grid=True)

class StaticSitemap(Sitemap):
    changefreq = 'Monthly'
    priority = 0.4
    location = 'contact/'

    def items(self):
        return reverse('contact')