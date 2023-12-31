# Generated by Django 4.2.6 on 2023-10-28 13:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_alter_billingaddress_date_alter_billingaddress_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 28, 13, 57, 15, 205832, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 28, 13, 57, 15, 205832, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=31)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 10, 28, 13, 57, 15, 212893, tzinfo=datetime.timezone.utc))),
                ('pieces_num', models.PositiveIntegerField(default=0)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bill'),
        ),
        migrations.DeleteModel(
            name='BillingAddress',
        ),
    ]
