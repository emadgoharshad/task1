from django.db import models

class Singer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birth_day = models.DateField()

    def __str__(self):
        return self.nickname

class Album(models.Model):
    name = models.CharField(max_length=50)
    main_singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    created_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField()
    genre = models.CharField(max_length=50)
    desc = models.TextField(blank=True,null=True)
    singers = models.ManyToManyField(Singer)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    created_date = models.DateField()

    def __str__(self):
        return self.name

class SongSinger(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE,related_name='song_singers')
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    start_time = models.DurationField()
    end_time = models.DurationField()























