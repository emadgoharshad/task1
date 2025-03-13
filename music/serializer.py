from rest_framework import serializers
from .models import Song, Singer, Album, SongSinger


class SongSingerSerializer(serializers.ModelSerializer):
    singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all())

    class Meta:
        model = SongSinger
        fields = ['singer', 'start_time', 'end_time']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'first_name', 'last_name', 'nickname', 'birth_day']


class AlbumSerializer(serializers.ModelSerializer):
    main_singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all())

    class Meta:
        model = Album
        fields = ['id', 'name', 'main_singer', 'created_date', 'price']


class SongSerializer(serializers.ModelSerializer):
    singers = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all(), many=True)
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    singers_info = SongSingerSerializer(source='song_singers', many=True, read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'genre', 'desc', 'singers', 'album', 'created_date', 'singers_info']

