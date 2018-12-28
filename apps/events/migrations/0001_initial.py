import apps.events.models

from django.conf import settings
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
        migrations.CreateModel(
            name='CompletedRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField(blank=True, max_length=500)),
                ('comment', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CubingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('wca', 'WCA events'), ('offline', 'Offline events')], default='offline', max_length=100)),
                ('non_wca_organizers', models.CharField(blank=True, max_length=200)),
                ('city_name', models.CharField(max_length=100)),
                ('registration_open', models.DateTimeField()),
                ('registration_close', models.DateTimeField()),
                ('registration_pay_open', models.DateTimeField(blank=True)),
                ('registration_pay_close', models.DateTimeField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('contact_number', models.BigIntegerField(blank=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('location', models.CharField(max_length=500)),
                ('attendant_limit', models.IntegerField(blank=True, default=1000)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('delegates', models.ManyToManyField(related_name='delagated_events', to=settings.AUTH_USER_MODEL)),
                ('events', models.ManyToManyField(to='results.Event')),
                ('registered', models.ManyToManyField(related_name='registered_events', through='events.CompletedRegistration', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PendingRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField(blank=True, max_length=500)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('cubing_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.CubingEvent')),
                ('events', models.ManyToManyField(to='results.Event')),
                ('user', models.OneToOneField(default='null', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cubingevent',
            name='waitlisted',
            field=models.ManyToManyField(related_name='waitlisted_events', through='events.PendingRegistration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cubingevent',
            name='wca_organizers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completedregistration',
            name='cubing_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.CubingEvent'),
        ),
        migrations.AddField(
            model_name='completedregistration',
            name='events',
            field=models.ManyToManyField(to='results.Event'),
        ),
        migrations.AddField(
            model_name='completedregistration',
            name='user',
            field=models.OneToOneField(default='null', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
