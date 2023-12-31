# Generated by Django 4.2.6 on 2023-10-31 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_billl_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billl',
            name='account_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='billl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 11, 24, 1, 902128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 11, 24, 1, 900112, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 11, 24, 1, 900112, tzinfo=datetime.timezone.utc)),
        ),
    ]
