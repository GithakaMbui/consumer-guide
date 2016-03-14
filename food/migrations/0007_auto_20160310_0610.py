# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20160307_2113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Forex',
        ),
        migrations.DeleteModel(
            name='Loans',
        ),
        migrations.AlterField(
            model_name='costs',
            name='itemname',
            field=models.CharField(max_length=200, choices=[(b'Jogoo Maize Flour', b'Jogoo Maize Flour'), (b'EX Wheat flour', b'EX Wheat flour'), (b'Mumias Sugar', b'Mumias Sugar'), (b'Kimbo Cooking Fat', b'Kimbo Cooking Fat'), (b'Broadways Whole Loaf', b'Broadways Whole Loaf')]),
        ),
        migrations.AlterField(
            model_name='costs',
            name='weight',
            field=models.IntegerField(default=1, choices=[(b'1', b'1 KG'), (b'2', b'2 KG'), (b'500', b'500 mg')]),
        ),
    ]
