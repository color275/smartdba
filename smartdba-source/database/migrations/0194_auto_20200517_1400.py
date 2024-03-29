# Generated by Django 2.1.5 on 2020-05-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0193_dblist_metareq_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='drop_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, verbose_name='삭제여부'),
        ),
        migrations.AlterField(
            model_name='dblist',
            name='exp_order',
            field=models.IntegerField(blank=True, default=999, null=True, verbose_name='화면노출순서'),
        ),
        migrations.AlterField(
            model_name='metareq',
            name='obj_class',
            field=models.CharField(choices=[('', '오브젝트 유형 선택'), ('1', 'TABLE(표준)'), ('2', 'TABLE(비표준)'), ('3', 'INDEX'), ('4', '권한'), ('5', 'PROCEDURE'), ('6', 'FUNCTION'), ('7', 'SEQUENCE'), ('8', 'PACKAGE'), ('9', '기타')], max_length=30, null=True, verbose_name='오브젝트 유형'),
        ),
        migrations.AlterField(
            model_name='metareq',
            name='obj_new',
            field=models.CharField(choices=[('', '신청 유형 선택'), ('1', '변경'), ('2', '신규'), ('3', '삭제')], max_length=30, null=True, verbose_name='변경 유형'),
        ),
    ]
