# Generated by Django 2.1.5 on 2020-05-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0182_projectlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectlist',
            name='reg_dtm',
        ),
        migrations.AddField(
            model_name='projectlist',
            name='start_dtm',
            field=models.DateField(default='now', verbose_name='프로젝트 시작 일자'),
            preserve_default=False,
        ),
    ]
