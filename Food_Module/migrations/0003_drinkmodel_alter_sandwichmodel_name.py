# Generated by Django 5.0.6 on 2024-07-04 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Module', '0002_sandwichmodel_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام نوشیدنی')),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='قیمت نوشیدنی')),
                ('image', models.ImageField(upload_to='drink')),
                ('offer_price', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, verbose_name='قیمت پس از تخفیف')),
                ('offer', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'نوشیدنی',
                'verbose_name_plural': 'نوشیدنی ها',
            },
        ),
        migrations.AlterField(
            model_name='sandwichmodel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام ساندویچ'),
        ),
    ]
