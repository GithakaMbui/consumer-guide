# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20160317_2206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instititution',
            new_name='Bureau',
        ),
        migrations.RenameField(
            model_name='bureau',
            old_name='Institution_type',
            new_name='bureau_type',
        ),
        migrations.RenameField(
            model_name='forex',
            old_name='instititution',
            new_name='bureau',
        ),
    ]
