# Generated by Django 3.2 on 2024-04-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_snackinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='snackinfo',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='snackinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
