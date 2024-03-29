# Generated by Django 3.0.6 on 2020-08-07 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0271_auto_20200731_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='stddomain',
            name='use_yn',
            field=models.CharField(blank=True, choices=[('1', '사용'), ('0', '미사용')], default='1', max_length=30, null=True, verbose_name='사용여부'),
        ),
        migrations.AlterField(
            model_name='metareq',
            name='id_domainanddblist',
            field=models.ForeignKey(blank=True, db_column='id_domainanddblist', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.DomainAndDbList', verbose_name='도메인명'),
        ),
        migrations.AlterField(
            model_name='weekdba',
            name='dba',
            field=models.CharField(blank=True, choices=[('22980', '이치호'), ('22764', '이정아'), ('22917', '정관호')], max_length=30, null=True, verbose_name='DBA'),
        ),
    ]
