# Generated by Django 5.0.7 on 2024-08-06 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='store')),
                ('taglin', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='slider')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.store')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.store')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('is_veg', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Food')),
                ('foodcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.foodcategory')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.store')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.storecategory'),
        ),
    ]
