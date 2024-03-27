from django.db import models


class Song(models.Model):
    song_name = models.CharField(max_length=10)
    lyricist = models.CharField(max_length=20)
    music_composer = models.CharField(max_length=20)
    from_movie = models.CharField(max_length=20)
    choice = [('t-series', 'T-SERIES'), ('zee music', 'ZEE MUSIC')]
    label = models.CharField(max_length=10, choices=choice)


