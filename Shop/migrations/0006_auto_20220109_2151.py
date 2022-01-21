# Generated by Django 3.2.9 on 2022-01-09 16:21

import Shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainslide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSSlug', models.CharField(max_length=150)),
                ('NNName', models.CharField(max_length=150)),
                ('PPProduct_image', models.ImageField(upload_to=Shop.models.get_file_path)),
                ('SSSmall_Description', models.CharField(max_length=300)),
                ('QQQuantity', models.IntegerField()),
                ('DDDescription', models.TextField(max_length=500)),
                ('OOOrignal_price', models.FloatField()),
                ('SSSelling_price', models.FloatField()),
                ('SSStatus', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
            ],
        ),
        migrations.RemoveField(
            model_name='con',
            name='number',
        ),
    ]