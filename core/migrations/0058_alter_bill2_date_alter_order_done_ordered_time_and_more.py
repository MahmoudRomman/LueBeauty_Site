# Generated by Django 4.2.6 on 2023-11-20 10:13

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_alter_bill2_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 10, 13, 49, 908714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 10, 13, 49, 908714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 10, 13, 49, 908714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='penality',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]