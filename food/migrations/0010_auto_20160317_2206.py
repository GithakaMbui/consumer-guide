# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20160317_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instititution',
            name='inst_name',
            field=models.CharField(default=b'SkyBureau', max_length=300, null=True, blank=True, choices=[(b'DTBBureau', b'DTBBureau'), (b'SkyBureau', b'SkyBureau'), (b'Nationalbureau', b'Nationalbureau'), (b'IMBureau', b'IMBureau'), (b'FinaBureau', b'FinaBureau')]),
        ),
    ]
