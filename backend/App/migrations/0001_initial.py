# Generated by Django 5.1.7 on 2025-04-03 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField(editable=False, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('party', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='candidate_photos/')),
                ('election_position', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('election_sign', models.ImageField(upload_to='election_sign/')),
            ],
        ),
        migrations.CreateModel(
            name='EthereumAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=42, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(default='none', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_voted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='voter_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
