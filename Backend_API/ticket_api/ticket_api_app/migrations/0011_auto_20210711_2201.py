# Generated by Django 3.2.5 on 2021-07-11 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0010_auto_20210710_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_db',
            name='owner',
        ),
        migrations.AddField(
            model_name='booking_db',
            name='booking_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight_one_db',
            name='booking_id',
            field=models.CharField(default='--NA--', max_length=100, null=True),
        ),
    ]
