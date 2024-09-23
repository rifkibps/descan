# Generated by Django 5.1 on 2024-09-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_familiesmodels_cleaned_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiesmodels',
            name='r206',
            field=models.CharField(choices=[('1', 'Terisi Lengkap'), ('2', 'Tidak Lengkap')], max_length=1, verbose_name='Hasil Pencacahan'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r309',
            field=models.CharField(blank=True, choices=[('1', 'Sendiri'), ('2', 'Bersama/Berkelompok'), ('3', 'MCK Umum'), ('4', 'Tidak Ada')], default='4', max_length=1, null=True, verbose_name='Fasilitas MCK'),
        ),
    ]
