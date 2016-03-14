# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0004_costs_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency_name', models.CharField(max_length=300)),
                ('buying_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loan_name', models.CharField(max_length=250)),
                ('loan_description', models.CharField(max_length=400)),
                ('requirements', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
