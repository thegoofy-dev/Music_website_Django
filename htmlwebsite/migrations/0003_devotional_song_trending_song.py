# Generated by Django 5.0.3 on 2024-03-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0002_rename_song_classical_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devotional_Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=5000)),
                ('artist', models.CharField(max_length=5000)),
                ('release_year', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=2000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/song_covers/')),
                ('song_file', models.FileField(upload_to='media/song_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Trending_Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=5000)),
                ('artist', models.CharField(max_length=5000)),
                ('release_year', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=2000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/song_covers/')),
                ('song_file', models.FileField(upload_to='media/song_files/')),
            ],
        ),
    ]