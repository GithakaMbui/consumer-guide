# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_auto_20160317_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='bank',
            field=models.CharField(default=b'Barclays', max_length=300, null=True, blank=True, choices=[(b'KSH', b'KSH'), (b'UGSH', b'UGSH'), (b'TZSH', b'UGSH'), (b'UGSH', b'UGSH'), (b'BPD', b'BPD'), (b'JYEN', b'JYEN')]),
        ),
    ]
