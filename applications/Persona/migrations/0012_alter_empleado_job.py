# Generated by Django 4.1.6 on 2023-02-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0011_alter_empleado_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('3', 'ECONOMISTA'), ('1', 'ADMINISTRADOR'), ('0', 'CONTADOR'), ('4', 'OTRO')], max_length=1, verbose_name='Trabajo'),
        ),
    ]