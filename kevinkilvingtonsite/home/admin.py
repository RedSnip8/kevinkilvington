from django.contrib import admin

from .models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id','client_name', 'photo_name', 'on_grid',)
    list_display_links = ('id', 'photo_name',)
    list_filter = ('client_name',)
    list_editable = ('on_grid',)

admin.site.register(Picture, PictureAdmin)