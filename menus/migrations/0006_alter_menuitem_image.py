# Generated by Django 5.0.7 on 2024-07-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
