# Generated by Django 5.0.6 on 2024-07-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurant_min_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
