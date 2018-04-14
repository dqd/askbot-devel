# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('django_authopenid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userassociation',
            name='meta',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='userpasswordqueue',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
