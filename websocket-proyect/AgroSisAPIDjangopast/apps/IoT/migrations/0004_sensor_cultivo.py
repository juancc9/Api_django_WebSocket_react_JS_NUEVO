# Generated by Django 5.1.3 on 2025-02-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT', '0003_remove_sensor_fk_bancal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='cultivo',
            field=models.CharField(default='Default cultivo', max_length=50),
        ),
    ]
