from django.urls import path

from .views import CreateView,AlbumListView,SingerSongView

urlpatterns = [
    path('create/',CreateView.as_view(),name='create'),
    path('albums/',AlbumListView.as_view(),name='albums'),
    path('singers/<int:singer_id>',SingerSongView.as_view(),name='singer_song')
]