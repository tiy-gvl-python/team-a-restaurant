# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='restaurant_app.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=300)),
                ('recommend', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)], max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('display', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('categories', models.ManyToManyField(to='restaurant_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField()),
                ('submit', models.BooleanField()),
                ('items', models.ManyToManyField(to='restaurant_app.Item', through='restaurant_app.Count')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('phone', models.CharField(max_length=17)),
                ('staff', models.BooleanField(default=False)),
                ('customer', models.BooleanField(default=True)),
                ('owner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'id',
                'verbose_name': 'id',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='restaurant_app.Profile'),
        ),
        migrations.AddField(
            model_name='count',
            name='item',
            field=models.ForeignKey(to='restaurant_app.Item'),
        ),
        migrations.AddField(
            model_name='count',
            name='order',
            field=models.ForeignKey(to='restaurant_app.Order'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='restaurant_app.Profile'),
        ),
        migrations.AddField(
            model_name='click',
            name='item',
            field=models.ForeignKey(to='restaurant_app.Item', null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='menu',
            field=models.ForeignKey(to='restaurant_app.Menu', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='items',
            field=models.ManyToManyField(to='restaurant_app.Item'),
        ),
    ]
