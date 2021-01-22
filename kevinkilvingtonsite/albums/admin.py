from django.contrib import admin

from .models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','Album_name', 'is_active')
    list_display_links = ('id', 'Album_name',)
    list_editable = ('is_active',)

admin.site.register(Album, AlbumAdmin)