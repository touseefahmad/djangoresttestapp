# Generated by Django 3.0.6 on 2021-07-14 17:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0018_booking_db_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_db',
            name='slug',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=12, unique=True),
        ),
    ]
