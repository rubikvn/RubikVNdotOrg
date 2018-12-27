# Generated by Django 2.1.2 on 2018-12-27 04:10

import apps.events.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=80, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('manage_competitions', models.BooleanField(default=False, null=True)),
                ('wca_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=80, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=80, null=True)),
                ('token_type', models.CharField(blank=True, max_length=20, null=True)),
                ('token_scope', models.CharField(blank=True, max_length=50, null=True)),
                ('token_created_at', models.IntegerField(blank=True, null=True)),
                ('token_expiry', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='results.Country')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.events.models.UserManager()),
            ],
        ),
    ]
