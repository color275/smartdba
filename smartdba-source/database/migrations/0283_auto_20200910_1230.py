# Generated by Django 3.0.6 on 2020-09-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0282_auto_20200831_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorManage',
            fields=[
            ],
            options={
                'verbose_name': '모니터링관리',
                'verbose_name_plural': '모니터링관리',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('database.dbdetail',),
        ),
        migrations.AlterModelOptions(
            name='monitoritemlist',
            options={'ordering': ['id_dbtype', 'exp_order'], 'verbose_name': '모니터링 항목', 'verbose_name_plural': '모니터링 항목'},
        ),
        migrations.AddField(
            model_name='stddomain',
            name='mod_dtm',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='수정일자'),
        ),
        migrations.AlterField(
            model_name='dbdetailmonitoritemlist',
            name='limit_value',
            field=models.CharField(blank=True, default='0', help_text='Health Cheack 일 경우 OPEN 으로 입력', max_length=100, null=True, verbose_name='임계치'),
        ),
        migrations.AlterField(
            model_name='tablelist',
            name='cdc_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, null=True, verbose_name='CDC대상여부'),
        ),
    ]
