# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=300)),
                ('recommend', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('display', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('categories', models.ManyToManyField(to='restaurant_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False)),
                ('phone', models.CharField(max_length=17)),
                ('staff', models.BooleanField(default=False)),
                ('customer', models.BooleanField(default=True)),
                ('owner', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'id',
                'verbose_name_plural': 'id',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='restaurant_app.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='restaurant_app.Profile'),
        ),
    ]
