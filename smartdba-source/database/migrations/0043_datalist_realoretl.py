# Generated by Django 2.1.5 on 2020-01-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0042_auto_20200125_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalist',
            name='realoretl',
            field=models.CharField(blank=True, choices=[('1', '실시간'), ('0', '분석')], default='0', max_length=100, null=True, verbose_name='실시간or분석'),
        ),
    ]
