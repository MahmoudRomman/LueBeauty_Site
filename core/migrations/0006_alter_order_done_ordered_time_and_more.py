# Generated by Django 4.2.6 on 2023-10-23 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_billingaddress_coupon_item_alter_product_density_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 10, 33, 36, 671028, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 10, 33, 36, 671028, tzinfo=datetime.timezone.utc)),
        ),
    ]
