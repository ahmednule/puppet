# Generated by Django 5.1.1 on 2024-10-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsystem', '0002_rename_pest_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pets',
            name='contact',
            field=models.IntegerField(default='0706703863'),
        ),
        migrations.AddField(
            model_name='pets',
            name='dislikes',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='pets',
            name='likes',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
