# Generated by Django 4.2.6 on 2023-10-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_addlink_date_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addlink',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
