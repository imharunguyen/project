# Generated by Django 4.0.4 on 2022-05-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_available_count',
        ),
    ]