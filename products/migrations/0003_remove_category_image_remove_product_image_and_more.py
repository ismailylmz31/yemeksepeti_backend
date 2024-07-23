# Generated by Django 5.0.6 on 2024-07-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]