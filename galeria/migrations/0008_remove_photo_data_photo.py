# Generated by Django 4.2.6 on 2023-10-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_photo_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='data_photo',
        ),
    ]