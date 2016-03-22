# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20160317_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forex',
            name='currency_name',
            field=models.CharField(max_length=300, choices=[(b'KSH', b'KSH'), (b'UGSH', b'UGSH'), (b'TZSH', b'UGSH'), (b'UGSH', b'UGSH'), (b'BPD', b'BPD'), (b'JYEN', b'JYEN')]),
        ),
    ]
