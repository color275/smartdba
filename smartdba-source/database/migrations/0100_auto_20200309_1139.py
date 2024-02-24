# Generated by Django 2.1.5 on 2020-03-09 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0099_auto_20200307_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequestTabPrivHist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approv_dtm', models.DateTimeField(blank=True, null=True, verbose_name='승인일자')),
                ('reg_dtm', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('priv', models.CharField(blank=True, max_length=100, null=True, verbose_name='권한')),
                ('req_reason', models.TextField(blank=True, max_length=4000, null=True, verbose_name='신청사유')),
                ('id_approver', models.ForeignKey(blank=True, db_column='id_approver', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id_approver_priv', to=settings.AUTH_USER_MODEL, verbose_name='승인자')),
                ('id_reg_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id_reg_user_priv', to=settings.AUTH_USER_MODEL, verbose_name='등록자')),
                ('id_userlist', models.ForeignKey(db_column='id_userlist', on_delete=django.db.models.deletion.PROTECT, to='database.UserList', verbose_name='User명')),
            ],
            options={
                'verbose_name': '[DBA-99] 테이블신청이력',
                'verbose_name_plural': '[DBA-99] 테이블신청이력',
                'db_table': 'cust_user_request_tab_priv_hist',
            },
        ),
        migrations.AlterField(
            model_name='columnlist',
            name='id_tablelist',
            field=models.ForeignKey(blank=True, db_column='id_tablelist', max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.TableList', verbose_name='테이블명'),
        ),
    ]
