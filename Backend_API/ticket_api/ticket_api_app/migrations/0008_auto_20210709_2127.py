# Generated by Django 3.2.5 on 2021-07-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0007_rename_seat_seat_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked_db',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='booked_db',
            name='seat_type',
        ),
    ]
