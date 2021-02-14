from django.urls import path

from . import views

urlpatterns = [
    path('', views.albums, name='albums'),
    path('<int:album_id>', views.events, name='events'),
    path('events/<int:event_id>', views.event, name='event')
]