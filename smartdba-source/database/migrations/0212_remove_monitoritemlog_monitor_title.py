# Generated by Django 2.1.5 on 2020-05-29 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0211_auto_20200529_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitoritemlog',
            name='monitor_title',
        ),
    ]
