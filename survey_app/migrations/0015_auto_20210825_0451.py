# Generated by Django 2.2.5 on 2021-08-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0014_auto_20210825_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.BigIntegerField(default=1629867101000),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.BigIntegerField(default=1629867101000),
        ),
        migrations.AlterField(
            model_name='log',
            name='created_at',
            field=models.BigIntegerField(default=1629867101000),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.BigIntegerField(default=1629867101000),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.BigIntegerField(default=1629867101000),
        ),
    ]