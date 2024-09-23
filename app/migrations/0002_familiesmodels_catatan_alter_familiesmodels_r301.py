# Generated by Django 5.1 on 2024-09-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiesmodels',
            name='catatan',
            field=models.TextField(blank=True, null=True, verbose_name='Catatan ...'),
        ),
        migrations.AlterField(
            model_name='familiesmodels',
            name='r301',
            field=models.CharField(choices=[('1', 'Milik Sendiri'), ('2', 'Kontrak/Sewa'), ('3', 'Bebas Sewa'), ('4', 'Dipinjami'), ('5', 'Dinas'), ('6', 'Lainnya')], max_length=1, verbose_name='Status penguasaan bangunan tempat tinggal yang ditempati'),
        ),
    ]