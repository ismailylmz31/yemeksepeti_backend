# Generated by Django 5.0.6 on 2024-07-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]