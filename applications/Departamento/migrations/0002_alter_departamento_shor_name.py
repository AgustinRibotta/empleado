# Generated by Django 4.1.6 on 2023-02-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
