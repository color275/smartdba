# Generated by Django 3.0.6 on 2020-06-08 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0243_stdattr_accept_yn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stdattr',
            name='id_dblist',
        ),
    ]
