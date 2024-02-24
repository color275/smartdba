# Generated by Django 2.1.5 on 2020-04-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0150_auto_20200403_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='metareq',
            name='obj_class',
            field=models.CharField(blank=True, choices=[('1', 'TABLE - 표준'), ('2', 'TABLE - 비표준'), ('3', 'SCRIPT')], default='1', max_length=30, null=True, verbose_name='오브젝트 유형'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='obj_new',
            field=models.CharField(blank=True, choices=[('1', 'TABLE - 표준'), ('2', 'TABLE - 비표준'), ('3', 'SCRIPT')], default='1', max_length=30, null=True, verbose_name='변경 유형'),
        ),
    ]
