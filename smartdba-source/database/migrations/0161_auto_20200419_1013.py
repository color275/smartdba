# Generated by Django 2.1.5 on 2020-04-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0160_auto_20200419_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='metareq',
            name='da_dev_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '반려')], max_length=200, null=True, verbose_name='DA개발승인승인여부'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='dba_dev_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '반려')], max_length=200, null=True, verbose_name='DBA개발승인승인여부'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='dba_prod_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '반려')], max_length=200, null=True, verbose_name='DBA운영승인승인여부'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='pl_dev_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '반려')], max_length=200, null=True, verbose_name='PL개발승인승인여부'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='pl_prod_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '반려')], max_length=200, null=True, verbose_name='PL운영승인승인여부'),
        ),
    ]
