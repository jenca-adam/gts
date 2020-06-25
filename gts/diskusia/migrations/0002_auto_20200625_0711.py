# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-06-25 07:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diskusia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prispevok',
            name='uzivatel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prispevky', to=settings.AUTH_USER_MODEL),
        ),
    ]
