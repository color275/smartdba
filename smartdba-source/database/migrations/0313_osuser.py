# Generated by Django 3.0.6 on 2020-12-01 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_safe_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0312_delete_osuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='OsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='OS계정명')),
                ('password', django_safe_fields.fields.SafeCharField(blank=True, max_length=256, null=True, verbose_name='비밀번호')),
                ('use_yn', models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='1', max_length=30, null=True, verbose_name='사용여부')),
                ('mod_dtm', models.DateTimeField(auto_now=True, null=True, verbose_name='수정일자')),
                ('id_dbdetail', models.ForeignKey(db_column='id_dbdetail', on_delete=django.db.models.deletion.CASCADE, to='database.DbDetail', verbose_name='DB상세')),
                ('id_mod_user', models.ForeignKey(blank=True, db_column='id_mod_user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='수정자')),
            ],
            options={
                'verbose_name': 'OS계정정보',
                'verbose_name_plural': 'OS계정정보',
                'db_table': 'cust_os_user',
            },
        ),
    ]
