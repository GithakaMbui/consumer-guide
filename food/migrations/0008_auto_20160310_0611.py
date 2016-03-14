# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20160310_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_name', models.CharField(max_length=300)),
                ('bank_type', models.CharField(max_length=300)),
                ('webpage', models.CharField(max_length=300)),
            ],
        ),
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
            name='Instititution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inst_name', models.CharField(default=b'SKY', max_length=300, null=True, blank=True)),
                ('webpage', models.CharField(max_length=300)),
                ('Institution_type', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loan_name', models.CharField(max_length=250)),
                ('loan_description', models.CharField(max_length=400)),
                ('requirements', models.CharField(max_length=300)),
                ('bank', models.ForeignKey(to='food.Banks')),
            ],
        ),
        migrations.AddField(
            model_name='forex',
            name='Instititution',
            field=models.ForeignKey(to='food.Instititution'),
        ),
    ]
