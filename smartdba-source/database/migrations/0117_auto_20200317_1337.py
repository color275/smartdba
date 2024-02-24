# Generated by Django 2.1.5 on 2020-03-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0116_auto_20200317_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnlist',
            name='drop_dtm',
            field=models.DateTimeField(blank=True, null=True, verbose_name='삭제일자'),
        ),
        migrations.AddField(
            model_name='columnlist',
            name='drop_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, verbose_name='삭제여부'),
        ),
    ]
