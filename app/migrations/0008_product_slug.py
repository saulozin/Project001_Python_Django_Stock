# Generated by Django 4.2.2 on 2023-06-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
