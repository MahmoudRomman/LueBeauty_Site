# Generated by Django 4.2.6 on 2023-10-31 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_billl_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 13, 36, 15, 751353, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 13, 36, 15, 749361, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 13, 36, 15, 749361, tzinfo=datetime.timezone.utc)),
        ),
    ]
