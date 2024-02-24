# Generated by Django 2.1.5 on 2020-02-16 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0073_auto_20200216_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datarequest',
            name='csr_no',
        ),
        migrations.AddField(
            model_name='datarequest',
            name='id_datalist',
            field=models.ForeignKey(blank=True, db_column='id_datalist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DataList', verbose_name='조회 데이터'),
        ),
    ]
