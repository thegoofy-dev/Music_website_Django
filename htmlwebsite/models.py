from django.db import models

# Create your models here.
class Classical_Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5000)
    artist = models.CharField(max_length=5000)
    movie_name = models.CharField(max_length=5000, null=True)
    release_year = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/song_covers/', null=True, blank=True)
    song_file = models.FileField(upload_to='media/song_files/')

    def __str__(self):
        return f"{self.title} by {self.artist} & Id:{self.song_id}"

class Trending_Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5000)
    artist = models.CharField(max_length=5000)
    movie_name = models.CharField(max_length=5000, null=True)
    release_year = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/song_covers/', null=True, blank=True)
    song_file = models.FileField(upload_to='media/song_files/')

    def __str__(self):
        return f"{self.title} by {self.artist} & Id:{self.song_id}"

class Devotional_Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5000)
    artist = models.CharField(max_length=5000)
    movie_name = models.CharField(max_length=5000, null=True)
    release_year = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/song_covers/', null=True, blank=True)
    song_file = models.FileField(upload_to='media/song_files/')

    def __str__(self):
        return f"{self.title} by {self.artist} & Id:{self.song_id}"

