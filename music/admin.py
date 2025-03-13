from django.contrib import admin

from .models import Song,Album,Singer,SongSinger

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Singer)
admin.site.register(SongSinger)