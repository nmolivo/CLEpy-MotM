# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 19:20
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180409_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelledOrder',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('app.order',),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=django_fsm.FSMField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('returned', 'Returned'), ('cancelled', 'Cancelled')], default='ordered', max_length=50),
        ),
    ]
