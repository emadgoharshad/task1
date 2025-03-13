from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Singer,Song,Album
from .serializer import SongSerializer,SingerSerializer,AlbumSerializer


class CreateView(APIView):
    def post(self,request):
        data_type = request.data.get('type')
        if data_type =='song':
            serializer = SongSerializer(data=request.data)
        elif data_type == 'album':
            serializer = AlbumSerializer(data=request.data)
        else:
            return Response({"error":"Invalid type"},status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AlbumListView(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)

class SingerSongView(APIView):
    def get(self,request,singer_id):
        songs = Song.objects.filter(singers__id=singer_id)
        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



