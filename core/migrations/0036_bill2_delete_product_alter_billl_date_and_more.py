# Generated by Django 4.2.6 on 2023-11-01 12:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0035_remove_f2_man_remove_f2_phone_alter_billl_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_phone_number', models.CharField(blank=True, max_length=31, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=31)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 11, 1, 12, 39, 53, 174512, tzinfo=datetime.timezone.utc))),
                ('account_name', models.CharField(blank=True, max_length=150, null=True)),
                ('wig_type', models.CharField(choices=[('اختر نوع الباروكة', 'اختر نوع الباروكة'), ('جذور امامية', 'جذور امامية'), ('جذور كامله', 'جذور كامله'), ('جذور دائرية 360', 'جذور دائرية 360')], max_length=150)),
                ('wig_long', models.CharField(choices=[('طول الباروكة', 'طول الباروكة'), ('12 Inch', '12 Inch'), ('14 Inch', '14 Inch'), ('16 Inch', '16 Inch'), ('18 Inch', '18 Inch'), ('20 Inch', '20 Inch'), ('22 Inch', '22 Inch'), ('24 Inch', '24 Inch'), ('26 Inch', '26 Inch'), ('28 Inch', '28 Inch'), ('30 Inch', '30 Inch'), ('32 Inch', '32 Inch'), ('34 Inch', '34 Inch'), ('36 Inch', '36 Inch'), ('38 Inch', '38 Inch'), ('40 Inch', '40 Inch')], max_length=150)),
                ('scalp_type', models.CharField(choices=[('اختر نوع الفروة', 'اختر نوع الفروة'), ('دانتيل', 'دانتيل'), ('حرير', 'حرير')], max_length=150)),
                ('wig_color', models.CharField(choices=[('اختر لون الباروكة', 'اختر لون الباروكة'), ('أسود طبيعى', 'أسود طبيعى'), ('بنى داكن', 'بنى داكن'), ('بنى فاتح', 'بنى فاتح'), ('اشقر', 'اشقر'), ('مخصل', 'مخصل')], max_length=150)),
                ('density', models.CharField(choices=[('اختر كثافة الباروكة', 'اختر كثافة الباروكة'), ('130', '130'), ('150', '150'), ('200', '200'), ('250', '250')], max_length=150)),
                ('price', models.IntegerField(default=1500)),
                ('pieces_num', models.PositiveIntegerField(default=0)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='billl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 12, 39, 53, 173482, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 12, 39, 53, 169111, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 12, 39, 53, 169111, tzinfo=datetime.timezone.utc)),
        ),
    ]
