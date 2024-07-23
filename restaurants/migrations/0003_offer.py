# Generated by Django 5.0.6 on 2024-07-23 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('is_exist', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='offers/')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='restaurants.restaurant')),
            ],
        ),
    ]