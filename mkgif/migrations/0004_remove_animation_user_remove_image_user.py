# Generated by Django 4.2.5 on 2023-09-15 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mkgif', '0003_alter_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
