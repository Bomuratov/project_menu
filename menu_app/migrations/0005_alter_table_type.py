# Generated by Django 4.2.7 on 2023-11-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_alter_table_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='type',
            field=models.CharField(choices=[('ELITE', 'ELITE'), ('PREMIUM', 'PREMIUM'), ('COMFORT', 'COMFORT'), ('BUSSINES', 'BUSSINES')], max_length=225),
        ),
    ]
