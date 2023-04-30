# Generated by Django 4.1.4 on 2023-04-29 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('startDate', models.DateTimeField(auto_now=True)),
                ('EndDate', models.DateField()),
                ('status', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('is_patent', models.BooleanField(default=False)),
                ('patent_info', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateField()),
                ('Storage_link', models.URLField(blank=True, null=True)),
                ('type', models.CharField(default='public', max_length=10)),
                ('description', models.TextField()),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.domain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('Storage_link', models.URLField(blank=True, null=True)),
                ('type', models.CharField(default='public', max_length=10)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('startDate', models.DateTimeField(auto_now=True)),
                ('EndDate', models.DateField()),
                ('status', models.CharField(max_length=7)),
                ('goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.goal')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('AicteMember', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AicteMember', to=settings.AUTH_USER_MODEL)),
                ('dean', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dean', to=settings.AUTH_USER_MODEL)),
                ('guid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guid', to=settings.AUTH_USER_MODEL)),
                ('hod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hod', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Approve',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_approved_guid', models.BooleanField(default=False)),
                ('is_aicte_approved', models.BooleanField(default=False)),
                ('is_hod_approved', models.BooleanField(default=False)),
                ('is_dean_approved', models.BooleanField(default=False)),
                ('description_guid', models.CharField(max_length=1000, null=True)),
                ('description_hod', models.CharField(max_length=1000, null=True)),
                ('description_dean', models.CharField(max_length=1000, null=True)),
                ('description_aicte', models.CharField(max_length=1000, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.AddConstraint(
            model_name='group',
            constraint=models.UniqueConstraint(fields=('name', 'student', 'project'), name='Unique_entries'),
        ),
    ]
