# Generated by Django 3.2.9 on 2022-01-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='creared_at',
            new_name='created_at',
        ),
    ]
