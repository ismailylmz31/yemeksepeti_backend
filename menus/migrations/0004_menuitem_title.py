# Generated by Django 5.0.7 on 2024-07-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_menu_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]