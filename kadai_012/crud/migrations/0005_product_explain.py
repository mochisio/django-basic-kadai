# Generated by Django 5.1.2 on 2024-11-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
    ]
