# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20160318_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='loan_amount',
            field=models.IntegerField(default=50000),
        ),
    ]
