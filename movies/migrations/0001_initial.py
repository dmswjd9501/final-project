# Generated by Django 2.2.7 on 2019-11-27 00:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.TextField()),
                ('actor_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('genre_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.TextField()),
                ('budget', models.TextField()),
                ('genres', models.TextField()),
                ('original_title', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.TextField()),
                ('poster_path', models.TextField()),
                ('release_date', models.TextField()),
                ('revenue', models.TextField()),
                ('runtime', models.TextField()),
                ('tagline', models.TextField()),
                ('title', models.CharField(max_length=150)),
                ('vote_average', models.FloatField()),
                ('actor_1', models.TextField()),
                ('actor_2', models.TextField()),
                ('actor_3', models.TextField()),
                ('actor_4', models.TextField()),
                ('actor_5', models.TextField()),
                ('director', models.CharField(max_length=45)),
                ('file_path_1', models.TextField()),
                ('file_path_2', models.TextField()),
                ('file_path_3', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
