# Generated by Django 3.2.9 on 2021-12-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='con',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('number', models.IntegerField()),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
