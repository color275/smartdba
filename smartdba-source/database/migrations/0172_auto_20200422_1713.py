# Generated by Django 2.1.5 on 2020-04-22 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0171_dbtablespace_id_dblist'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaGrantDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='권한')),
                ('crud', models.CharField(blank=True, max_length=100, null=True, verbose_name='CRUD')),
                ('reg_dtm', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
            ],
            options={
                'verbose_name': '[DBA-99] 변경관리 권한 상세',
                'verbose_name_plural': '[DBA-99] 변경관리 권한 상세',
                'db_table': 'cust_meta_grant_detail',
            },
        ),
        migrations.RemoveField(
            model_name='metagrantlist',
            name='crud',
        ),
        migrations.RemoveField(
            model_name='metagrantlist',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='metagrantlist',
            name='role',
        ),
        migrations.AlterField(
            model_name='dbowner',
            name='id_dblist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbList', verbose_name='DB명'),
        ),
        migrations.AlterField(
            model_name='dbtablespace',
            name='id_dblist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbList', verbose_name='DB명'),
        ),
        migrations.AlterField(
            model_name='dbtablespace',
            name='id_owner',
            field=models.ForeignKey(blank=True, db_column='id_owner', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DBOwner', verbose_name='OWNER명'),
        ),
        migrations.AlterField(
            model_name='metagrantlist',
            name='id_dblist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbList', verbose_name='DB명'),
        ),
        migrations.AlterField(
            model_name='metagrantlist',
            name='id_reg_user',
            field=models.ForeignKey(blank=True, db_column='id_reg_user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='등록자'),
        ),
        migrations.AddField(
            model_name='metagrantdetail',
            name='id_metagrantlist',
            field=models.ForeignKey(blank=True, db_column='id_metagrantlist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.MetaGrantList', verbose_name='서비스명'),
        ),
        migrations.AddField(
            model_name='metagrantdetail',
            name='id_reg_user',
            field=models.ForeignKey(blank=True, db_column='id_reg_user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='등록자'),
        ),
    ]
