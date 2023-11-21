# Generated by Django 4.2.6 on 2023-11-08 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_alter_bill2_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 9, 12, 12, 459698, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 9, 12, 12, 459698, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 9, 12, 12, 459698, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(max_length=31, unique=True),
        ),
    ]