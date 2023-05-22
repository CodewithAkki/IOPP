# Generated by Django 4.1.4 on 2023-05-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_githublink'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='exprience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
