# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181018_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='haveAnimal',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True),
        ),
    ]
