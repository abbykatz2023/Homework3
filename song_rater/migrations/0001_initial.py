# Generated by Django 4.0.2 on 2022-04-04 23:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('hometown', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=200)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song_rater.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song_rater.song')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song_rater.user')),
            ],
        ),
    ]
