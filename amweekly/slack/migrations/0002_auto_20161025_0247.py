# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incomingwebhook',
            name='webhook_transaction',
        ),
        migrations.RemoveField(
            model_name='webhooktransaction',
            name='generated_at',
        ),
    ]
