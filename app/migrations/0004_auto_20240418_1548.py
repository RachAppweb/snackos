# Generated by Django 3.2 on 2024-04-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20240418_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snackinfo',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='snackinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/snack'),
        ),
        migrations.AlterField(
            model_name='snackinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
