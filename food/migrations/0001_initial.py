# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemname', models.CharField(max_length=200)),
                ('unitcost', models.IntegerField()),
                ('dateprovided', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
