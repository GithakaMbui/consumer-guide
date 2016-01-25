# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_outlet_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='costs',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]
