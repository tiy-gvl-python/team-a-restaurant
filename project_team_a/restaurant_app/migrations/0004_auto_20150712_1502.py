# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0003_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=300)),
                ('recommend', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='restaurant_app.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
