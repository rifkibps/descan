# Generated by Django 5.1 on 2024-08-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_populationsmodels_r430_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504a',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah ternak Sapi (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504b',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah ternak Kerbau (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504c',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah ternak Kuda (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504d',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah ternak Babi (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504e',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah ternak Kambing/Domba (ekor)?'),
        ),
    ]