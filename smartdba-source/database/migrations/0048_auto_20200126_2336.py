# Generated by Django 2.1.5 on 2020-01-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0047_auto_20200126_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuninglist',
            name='sql_id',
            field=models.CharField(max_length=100, null=True, verbose_name='SQL_ID'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='제목'),
        ),
    ]
