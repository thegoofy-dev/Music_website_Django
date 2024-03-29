# Generated by Django 5.0.3 on 2024-03-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
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