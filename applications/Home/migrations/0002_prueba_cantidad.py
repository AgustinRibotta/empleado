# Generated by Django 4.1.6 on 2023-02-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]