# Generated by Django 2.2.15 on 2020-10-04 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('encrypted_login', '0002_authchecker_q_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='authchecker',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 17, 22, 14, 385647, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
