# Generated by Django 4.1.7 on 2023-05-01 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_rename_reviews_review_remove_movie_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.movie'),
        ),
    ]