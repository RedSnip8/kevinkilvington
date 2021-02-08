from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','f_name', 'l_name', 'request_date', 'phone_number',)
    list_display_links = ('id', 'f_name', 'l_name',)
    list_filter = ('l_name', 'request_date', 'phone_number')
    

admin.site.register(Contact, ContactAdmin)
