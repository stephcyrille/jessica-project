# Generated by Django 2.2.15 on 2020-09-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypted_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authchecker',
            name='q_code',
            field=models.CharField(default=444444, max_length=6),
            preserve_default=False,
        ),
    ]