# Generated by Django 3.0.6 on 2020-07-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0258_dbdetail_conct_succs_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdattr',
            name='use_yn',
            field=models.CharField(blank=True, choices=[('1', '사용'), ('0', '미사용')], default='1', max_length=30, null=True, verbose_name='사용여부'),
        ),
    ]
