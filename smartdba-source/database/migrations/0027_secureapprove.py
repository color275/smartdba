# Generated by Django 2.1.5 on 2020-01-21 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_datalist_privacy_yn'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecureApprove',
            fields=[
            ],
            options={
                'verbose_name': '99.보안센터-데이터노출승인',
                'verbose_name_plural': '99.보안센터-데이터노출승인',
                'proxy': True,
                'indexes': [],
            },
            bases=('database.datalist',),
        ),
    ]
