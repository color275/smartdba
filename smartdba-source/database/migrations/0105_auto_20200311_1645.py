# Generated by Django 2.1.5 on 2020-03-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0104_auto_20200309_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablelist',
            name='table_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='테이블 물리명'),
        ),
    ]
