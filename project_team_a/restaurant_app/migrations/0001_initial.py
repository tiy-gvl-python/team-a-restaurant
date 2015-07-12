# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
=======
import django.core.validators
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('name', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='restaurant_app.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=300)),
                ('recommend', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=12, decimal_places=2, validators=django.core.validators.MinValueValidator(0.01))),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('display', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('categories', models.ManyToManyField(to='restaurant_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField()),
                ('submit', models.BooleanField()),
                ('items', models.ManyToManyField(through='restaurant_app.Count', to='restaurant_app.Item')),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField()),
                ('submit', models.BooleanField()),
                ('items', models.ManyToManyField(to='restaurant_app.Item', through='restaurant_app.Count')),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
                ('phone', models.CharField(max_length=17)),
                ('staff', models.BooleanField(default=False)),
                ('customer', models.BooleanField(default=True)),
                ('owner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
<<<<<<< HEAD
                'verbose_name': 'id',
                'verbose_name_plural': 'id',
                'ordering': ['id'],
=======
                'verbose_name_plural': 'id',
                'ordering': ['id'],
                'verbose_name': 'id',
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
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
<<<<<<< HEAD
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='restaurant_app.Profile'),
        ),
        migrations.AddField(
=======
>>>>>>> bf78187b9df383faefefeb80f8893eb7aefaed6d
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
