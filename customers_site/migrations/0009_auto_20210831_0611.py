# Generated by Django 2.2.5 on 2021-08-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_site', '0008_auto_20210831_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.BigIntegerField(default=1630390289000),
        ),
        migrations.AlterField(
            model_name='preference',
            name='created_at',
            field=models.BigIntegerField(default=1630390289000),
        ),
        migrations.AlterField(
            model_name='preference',
            name='updated_at',
            field=models.BigIntegerField(default=1630390289000),
        ),
    ]
