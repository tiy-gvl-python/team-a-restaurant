# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, to='restaurant_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('display', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('categories', models.ManyToManyField(to='restaurant_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField()),
                ('submit', models.BooleanField()),
                ('items', models.ManyToManyField(through='restaurant_app.Count', to='restaurant_app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('phone', models.CharField(max_length=17)),
                ('staff', models.BooleanField(default=False)),
                ('customer', models.BooleanField(default=True)),
                ('owner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
            model_name='click',
            name='item',
            field=models.ForeignKey(null=True, to='restaurant_app.Item'),
        ),
        migrations.AddField(
            model_name='click',
            name='menu',
            field=models.ForeignKey(null=True, to='restaurant_app.Menu'),
        ),
        migrations.AddField(
            model_name='category',
            name='items',
            field=models.ManyToManyField(to='restaurant_app.Item'),
        ),
    ]
