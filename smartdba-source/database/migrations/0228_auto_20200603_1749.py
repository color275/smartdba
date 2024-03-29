# Generated by Django 3.0.6 on 2020-06-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0227_dbdetail_slave_yn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbdetail',
            old_name='slave_yn',
            new_name='ha_case',
        ),
        migrations.AlterField(
            model_name='dbdetail',
            name='active_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='1', max_length=30, null=True, verbose_name='Active(Open)여부'),
        ),
    ]
