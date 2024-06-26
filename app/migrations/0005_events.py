# Generated by Django 3.2 on 2024-04-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240418_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/snack')),
                ('description', models.TextField()),
            ],
        ),
    ]
