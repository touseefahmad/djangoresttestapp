# Generated by Django 3.0.6 on 2021-07-14 17:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_api_app', '0019_auto_20210714_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_db',
            name='slug',
        ),
        migrations.AlterField(
            model_name='booking_db',
            name='booking_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=12, unique=True),
        ),
    ]
