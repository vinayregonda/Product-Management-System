# Generated by Django 5.0.1 on 2024-02-02 07:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]