# Generated by Django 2.1.5 on 2020-05-29 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0206_auto_20200529_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbdetailmonitoritemlist',
            name='id_dbdetail',
        ),
        migrations.RemoveField(
            model_name='dbdetailmonitoritemlist',
            name='id_monitoritemlist',
        ),
        migrations.RemoveField(
            model_name='dbdetailmonitoritemlist',
            name='id_reg_user',
        ),
        migrations.RemoveField(
            model_name='dbdetail',
            name='id_monitoritemlist',
        ),
        migrations.DeleteModel(
            name='DBDetailMonitorItemList',
        ),
    ]
