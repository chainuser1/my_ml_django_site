# Generated by Django 2.2.5 on 2021-08-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_site', '0003_auto_20210825_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.BigIntegerField(default=1629867150000),
        ),
        migrations.AlterField(
            model_name='preference',
            name='created_at',
            field=models.BigIntegerField(default=1629867150000),
        ),
        migrations.AlterField(
            model_name='preference',
            name='updated_at',
            field=models.BigIntegerField(default=1629867150000),
        ),
    ]