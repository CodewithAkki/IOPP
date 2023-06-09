# Generated by Django 4.1.4 on 2023-05-20 05:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('UniversityName', models.CharField(default=' ', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('collegeName', models.CharField(default=' ', max_length=200, null=True)),
                ('Type', models.CharField(default=' ', max_length=200, null=True)),
                ('University', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.university')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=' ', max_length=200, null=True)),
                ('last_name', models.CharField(default=' ', max_length=200, null=True)),
                ('department', models.CharField(blank=True, default=' ', max_length=200, null=True)),
                ('phone_no', models.CharField(default=None, max_length=15, null=True)),
                ('address', models.CharField(default=' ', max_length=200, null=True)),
                ('birthdate', models.DateField(default=None, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('profilePic', models.URLField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')),
                ('registerDate', models.DateField(auto_now=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.college')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.university')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
