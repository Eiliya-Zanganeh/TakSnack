# Generated by Django 5.0.6 on 2024-07-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Module', '0003_drinkmodel_alter_sandwichmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SauceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام سس')),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='قیمت سس')),
                ('image', models.ImageField(upload_to='sauce')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'سس',
                'verbose_name_plural': 'سس ها',
            },
        ),
    ]
