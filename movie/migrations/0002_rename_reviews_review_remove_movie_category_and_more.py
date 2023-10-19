# Generated by Django 4.1.7 on 2023-03-17 15:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
