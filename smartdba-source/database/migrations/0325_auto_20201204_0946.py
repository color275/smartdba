# Generated by Django 3.0.6 on 2020-12-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0324_auto_20201203_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbuser',
            name='drop_dtm',
            field=models.DateTimeField(blank=True, null=True, verbose_name='삭제일자'),
        ),
        migrations.AddField(
            model_name='dbuser',
            name='drop_yn',
            field=models.CharField(choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, null=True, verbose_name='삭제여부'),
        ),
    ]
