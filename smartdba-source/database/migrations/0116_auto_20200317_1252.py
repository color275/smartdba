# Generated by Django 2.1.5 on 2020-03-17 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0115_auto_20200317_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectsource',
            name='id_objectlist',
        ),
        migrations.RemoveField(
            model_name='objectsource',
            name='oper_cd',
        ),
        migrations.DeleteModel(
            name='ObjectSource',
        ),
    ]
