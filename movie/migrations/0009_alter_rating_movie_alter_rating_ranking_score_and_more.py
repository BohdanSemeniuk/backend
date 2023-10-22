# Generated by Django 4.1.7 on 2023-10-22 13:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0008_alter_rating_movie_alter_rating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ranking_score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]