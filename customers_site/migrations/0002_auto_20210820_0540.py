# Generated by Django 2.2.5 on 2021-08-20 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='like_dislike',
            new_name='like',
        ),
        migrations.AddField(
            model_name='preference',
            name='created_at',
            field=models.BigIntegerField(default=1629438025000),
        ),
        migrations.AddField(
            model_name='preference',
            name='product_category',
            field=models.PositiveIntegerField(choices=[(7, 'Grains, Nuts, and Beans'), (8, 'Leafy Vegetables'), (9, 'Meat, Fish, and Poultry Products'), (10, 'Root Crops, Mushrooms'), (11, 'Fruits'), (12, 'Sugar & Sweeteners')], null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='product_name',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='updated_at',
            field=models.BigIntegerField(default=1629438025000),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.BigIntegerField(default=1629438025000),
        ),
        migrations.AlterField(
            model_name='preference',
            name='product',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='survey_app.Product'),
        ),
    ]