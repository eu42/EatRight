# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20161204_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
        migrations.AlterField(
            model_name='food',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
