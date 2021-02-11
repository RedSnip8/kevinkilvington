from django.contrib import admin

from .models import Album, Events

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','Album_name', 'is_active')
    list_display_links = ('id', 'Album_name',)
    list_editable = ('is_active',)

admin.site.register(Album, AlbumAdmin)

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'event_year', 'is_active')
    list_display_links = ('id', 'event_name')
    list_editable = ('is_active', 'event_year')

admin.site.register(Events, EventsAdmin)