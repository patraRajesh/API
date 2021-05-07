# Generated by Django 3.2.1 on 2021-05-07 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='song',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]