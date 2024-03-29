# Generated by Django 5.0.3 on 2024-03-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0003_devotional_song_trending_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='classical_song',
            name='movie_name',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='devotional_song',
            name='movie_name',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='trending_song',
            name='movie_name',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
