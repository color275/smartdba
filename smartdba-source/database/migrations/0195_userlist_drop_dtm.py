# Generated by Django 2.1.5 on 2020-05-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0194_auto_20200517_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='drop_dtm',
            field=models.DateTimeField(blank=True, null=True, verbose_name='삭제일자'),
        ),
    ]
