# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2),
        ),
    ]
