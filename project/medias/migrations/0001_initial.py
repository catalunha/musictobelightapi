# Generated by Django 5.0 on 2023-12-09 18:07

import django.db.models.deletion
import project.medias.models.audio
import project.medias.models.image
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('audio', models.FileField(upload_to=project.medias.models.audio.Audio.uploadTo)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('extension', models.CharField(blank=True, max_length=25, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audiosmedia', to='accounts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=project.medias.models.image.Image.uploadTo)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('extension', models.CharField(blank=True, max_length=25, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imagesmedia', to='accounts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
