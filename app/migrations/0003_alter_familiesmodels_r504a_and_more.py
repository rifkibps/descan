# Generated by Django 5.1 on 2024-08-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_familiesmodels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504a',
            field=models.IntegerField(default=0, verbose_name='Jumlah ternak Sapi (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504b',
            field=models.IntegerField(default=0, verbose_name='Jumlah ternak Kerbau (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504c',
            field=models.IntegerField(default=0, verbose_name='Jumlah ternak Kuda (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504d',
            field=models.IntegerField(default=0, verbose_name='Jumlah ternak Babi (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r504e',
            field=models.IntegerField(default=0, verbose_name='Jumlah ternak Kambing/Domba (ekor)?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r505',
            field=models.CharField(choices=[('0', 'Tidak Menggunakan Internet'), ('1', 'Internet dan TV Digital Berlangganan'), ('2', 'WiFi'), ('3', 'Internet Handphone')], max_length=1, verbose_name='Jenis akses internet utama yang digunakan oleh keluarga?'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r506',
            field=models.CharField(choices=[('1', 'Ya, untuk Usaha'), ('2', 'Ya, untuk Pribadi'), ('3', 'Ya, untuk usaha dan pribadi'), ('4', 'Tidak')], max_length=1, verbose_name='Apakah keluarga ini memiliki rekening aktif atau dompet digital?'),
        ),
    ]