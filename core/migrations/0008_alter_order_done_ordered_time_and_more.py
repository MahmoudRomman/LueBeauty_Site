# Generated by Django 4.2.6 on 2023-10-24 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_item_discount_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 9, 1, 10, 101664, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 9, 1, 10, 101664, tzinfo=datetime.timezone.utc)),
        ),
    ]
