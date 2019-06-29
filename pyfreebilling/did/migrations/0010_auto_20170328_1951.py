# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-28 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('did', '0009_did_insee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routesdid',
            name='type',
            field=models.CharField(choices=[(b's', 'SIP Trunk'), (b'e', 'External number')], default=b'm', help_text='Routing type : sip trunk (s) or\n                                external number (e).', max_length=2, verbose_name='Route type'),
        ),
    ]