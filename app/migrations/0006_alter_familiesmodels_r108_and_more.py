# Generated by Django 5.1 on 2024-09-08 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_populationsmodels_r520a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiesmodels',
            name='r108',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='Nomor Kartu Keluarga (KK)'),
        ),
        migrations.AlterField(
            model_name='populationsmodels',
            name='r502',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='NIK'),
        ),
    ]
