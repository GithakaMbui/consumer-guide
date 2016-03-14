# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_forex_loans_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='retailer',
            field=models.CharField(max_length=200, choices=[(b'Nakumatt', b'Nakumatt'), (b'Tuskys', b'Tuskys'), (b'Naivas', b'Naivas'), (b'Ukwala', b'Ukwala'), (b'Uchumi', b'Uchumi')]),
        ),
    ]
