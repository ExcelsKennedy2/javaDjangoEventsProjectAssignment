# Generated by Django 5.0.2 on 2024-11-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(),
        ),
    ]
