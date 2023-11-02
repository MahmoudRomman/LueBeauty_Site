# Generated by Django 4.2.6 on 2023-11-02 09:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_bill2_delete_product_alter_billl_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill2',
            name='customer_name',
            field=models.CharField(default='ahmed', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 9, 15, 4, 650486, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bill2'),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 9, 15, 4, 648485, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 9, 15, 4, 648485, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Billl',
        ),
    ]