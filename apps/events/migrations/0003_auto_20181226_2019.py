# Generated by Django 2.1.2 on 2018-12-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181226_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wca_id',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
