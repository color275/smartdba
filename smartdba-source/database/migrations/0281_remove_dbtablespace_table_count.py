# Generated by Django 3.0.6 on 2020-08-27 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0280_dbtablespace_table_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbtablespace',
            name='table_count',
        ),
    ]
