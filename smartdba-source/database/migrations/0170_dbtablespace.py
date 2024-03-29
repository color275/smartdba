# Generated by Django 2.1.5 on 2020-04-22 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0169_auto_20200421_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBTablespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablespace_name', models.CharField(default='', max_length=100, verbose_name='테이블스페이스명')),
                ('id_owner', models.ForeignKey(blank=True, db_column='id_owner', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.DBOwner', verbose_name='OWNER명')),
            ],
            options={
                'verbose_name': '[DBA-99] DB TBS명',
                'verbose_name_plural': '[DBA-99] DB TBS명',
                'db_table': 'cust_tablespace',
            },
        ),
    ]
