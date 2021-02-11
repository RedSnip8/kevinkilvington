from django.contrib import admin

from .models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_name', 'photo_album', 'event_name', 'on_grid', 'album_cover')
    list_display_links = ('id', 'photo_name',)
    list_filter = ('client_name', 'photo_album', 'album_cover')
    list_editable = ('on_grid','photo_album', 'album_cover', 'event_name')

admin.site.register(Picture, PictureAdmin)