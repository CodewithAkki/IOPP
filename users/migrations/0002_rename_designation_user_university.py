# Generated by Django 4.1.4 on 2023-05-07 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='designation',
            new_name='university',
        ),
    ]