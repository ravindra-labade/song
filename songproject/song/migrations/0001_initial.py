# Generated by Django 5.0.3 on 2024-03-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=10)),
                ('lyricist', models.CharField(max_length=20)),
                ('music_composer', models.CharField(max_length=20)),
                ('from_movie', models.CharField(max_length=20)),
                ('label', models.CharField(choices=[('t-series', 'T-SERIES'), ('zee music', 'ZEE MUSIC')], max_length=10)),
            ],
        ),
    ]
