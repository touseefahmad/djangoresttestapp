# Generated by Django 3.2.5 on 2021-07-11 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0012_auto_20210711_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_db',
            name='booking_name',
        ),
    ]
