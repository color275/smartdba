# Generated by Django 2.1.5 on 2020-01-11 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_databasemap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databasemap',
            name='id_dblist',
        ),
        migrations.RemoveField(
            model_name='databasemap',
            name='id_domain',
        ),
        migrations.DeleteModel(
            name='DatabaseMap',
        ),
    ]
