# Generated by Django 2.1.5 on 2020-01-22 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0033_auto_20200122_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainAndDbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_dtm', models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록일자')),
                ('mod_dtm', models.DateTimeField(auto_now=True, null=True, verbose_name='수정일자')),
                ('id_dblist', models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.DbList', verbose_name='DB명')),
                ('id_domain', models.ForeignKey(blank=True, db_column='id_domain', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.Domain', verbose_name='도메인명')),
                ('id_mod_user', models.ForeignKey(blank=True, db_column='id_mod_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DomainAndDbList_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='수정자')),
                ('id_reg_user', models.ForeignKey(blank=True, db_column='id_reg_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DomainAndDbList_reg_user', to=settings.AUTH_USER_MODEL, verbose_name='등록자')),
            ],
            options={
                'verbose_name': '[DBA-01] 도메인-데이터베이스 매핑',
                'verbose_name_plural': '[DBA-01] 도메인-데이터베이스 매핑',
                'db_table': 'cust_db_domain_mapping',
            },
        ),
    ]
