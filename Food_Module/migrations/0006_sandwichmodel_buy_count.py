# Generated by Django 5.0.6 on 2024-07-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Module', '0005_sandwichmodel_is_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwichmodel',
            name='buy_count',
            field=models.IntegerField(default=0, verbose_name='تعداد فروش'),
        ),
    ]
