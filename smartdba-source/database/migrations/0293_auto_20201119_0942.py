# Generated by Django 3.0.6 on 2020-11-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0292_auto_20201118_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainanddblist',
            name='erd_user',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='ERD계정명'),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='exp_order',
            field=models.IntegerField(blank=True, default=99, help_text='같은 DB 내 도메인 노출 순서', null=True, verbose_name='DB 별 화면노출순서'),
        ),
    ]
