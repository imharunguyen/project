# Generated by Django 4.0.2 on 2022-05-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_product_product_available_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_available_count',
            field=models.IntegerField(default=0),
        ),
    ]
