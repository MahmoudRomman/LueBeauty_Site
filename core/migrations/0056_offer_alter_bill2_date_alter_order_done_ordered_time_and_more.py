# Generated by Django 4.2.6 on 2023-11-13 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_alter_bill2_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offer', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 9, 44, 15, 488043, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 9, 44, 15, 481868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 9, 44, 15, 481868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(choices=[('5555555555', '5555555555'), ('4444444444444', '4444444444444'), ('222222222222', '222222222222'), ('111111111', '111111111'), ('33333333333333333', '33333333333333333'), ('666666666666666', '666666666666666'), ('777777777777777', '777777777777777')], max_length=31),
        ),
    ]
