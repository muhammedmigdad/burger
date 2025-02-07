# Generated by Django 5.0.7 on 2024-08-19 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_address_address_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbill',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('work', 'work'), ('other', 'other'), ('home', 'home')], max_length=255),
        ),
    ]
