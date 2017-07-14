# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20170608_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='kind',
            field=models.CharField(choices=[('email', 'Email'), ('webhook', 'Webhook'), ('hipchat', 'HipChat'), ('slack', 'Slack'), ('pd', 'PagerDuty'), ('po', 'Pushover'), ('pushbullet', 'Pushbullet'), ('opsgenie', 'OpsGenie'), ('victorops', 'VictorOps'), ('discord', 'Discord'), ('telegram', 'Telegram'), ('sms', 'SMS')], max_length=20),
        ),
    ]
