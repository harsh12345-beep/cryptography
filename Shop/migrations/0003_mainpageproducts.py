# Generated by Django 3.2.9 on 2021-12-24 07:11

import Shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_con'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAINPAGEPRODUCTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSlug', models.CharField(max_length=150)),
                ('NName', models.CharField(max_length=150)),
                ('PProduct_image', models.ImageField(upload_to=Shop.models.get_file_path)),
                ('SSmall_Description', models.CharField(max_length=300)),
                ('QQuantity', models.IntegerField()),
                ('DDescription', models.TextField(max_length=500)),
                ('OOrignal_price', models.FloatField()),
                ('SSelling_price', models.FloatField()),
                ('SStatus', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
                ('TTrending', models.BooleanField(default=False, help_text='0=default, 1=trending')),
                ('TTag', models.CharField(max_length=300)),
                ('MMeta_title', models.CharField(max_length=150)),
                ('MMeta_keywords', models.CharField(max_length=150)),
                ('MMeta_description', models.TextField(max_length=500)),
                ('CCreated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
