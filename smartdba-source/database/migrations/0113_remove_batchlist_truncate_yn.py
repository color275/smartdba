# Generated by Django 2.1.5 on 2020-03-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0112_auto_20200317_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchlist',
            name='truncate_yn',
        ),
    ]
