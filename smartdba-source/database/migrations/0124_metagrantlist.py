# Generated by Django 2.1.5 on 2020-03-23 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0123_auto_20200320_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaGrantList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=100, null=True, verbose_name='owner')),
                ('app_service', models.CharField(blank=True, max_length=100, null=True, verbose_name='서비스')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='권한')),
                ('crud', models.CharField(blank=True, max_length=100, null=True, verbose_name='CRUD')),
                ('reg_dtm', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('id_dblist', models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.DbList', verbose_name='DB명')),
                ('id_reg_user', models.ForeignKey(blank=True, db_column='id_reg_user', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='등록자')),
            ],
            options={
                'verbose_name': '[DBA-99] 변경관리 권한 리스트',
                'verbose_name_plural': '[DBA-99] 변경관리 권한 리스트',
                'db_table': 'cust_meta_grant_list',
            },
        ),
    ]
