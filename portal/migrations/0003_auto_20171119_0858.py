# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_teachaprofile_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachaprofile',
            name='notes',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
