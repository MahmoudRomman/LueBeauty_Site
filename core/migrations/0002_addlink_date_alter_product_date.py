# Generated by Django 4.2.6 on 2023-10-21 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addlink',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 21, 11, 54, 58, 445870)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 21, 11, 54, 58, 444873)),
        ),
    ]
