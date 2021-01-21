from django.contrib import admin

from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id','service_name', 'is_availible',)
    list_display_links = ('id', 'service_name',)
    list_filter = ('service_name',)
    list_editable = ('is_availible',)

admin.site.register(Services, ServicesAdmin)
