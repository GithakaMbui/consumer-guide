# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20160310_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forex',
            old_name='Instititution',
            new_name='instititution',
        ),
        migrations.AlterField(
            model_name='costs',
            name='itemname',
            field=models.CharField(max_length=200, choices=[(b'Jogoo Maize Flour', b'Jogoo Maize Flour'), (b'EX Wheat flour', b'EX Wheat flour'), (b'Sugar', b'Sugar'), (b'Kimbo Cooking Fat', b'Kimbo Cooking Fat'), (b'Broadways Whole Loaf', b'Broadways Whole Loaf')]),
        ),
    ]
