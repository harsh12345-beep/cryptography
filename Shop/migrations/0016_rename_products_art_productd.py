# Generated by Django 3.2.9 on 2022-01-14 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_rename_product_art_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='products',
            new_name='productd',
        ),
    ]