from django.contrib import admin

from .models import Photographer

class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'is_active',)
    list_display_links = ('id', 'first_name',)
    list_filter = ('first_name',)
    list_editable = ('is_active',)

admin.site.register(Photographer, PhotographerAdmin)
