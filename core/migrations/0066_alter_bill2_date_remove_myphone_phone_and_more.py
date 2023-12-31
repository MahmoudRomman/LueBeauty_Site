# Generated by Django 4.2.6 on 2023-11-22 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_alter_bill2_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 22, 14, 38, 48, 680786, tzinfo=datetime.timezone.utc)),
        ),
        migrations.RemoveField(
            model_name='myphone',
            name='phone',
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 22, 14, 38, 48, 678989, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 22, 14, 38, 48, 678989, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='myphone',
            name='phone',
            field=models.ManyToManyField(to='core.phones'),
        ),
    ]
