# Generated by Django 3.0.6 on 2020-08-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0279_dbowner_table_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbtablespace',
            name='table_count',
            field=models.IntegerField(default=0, verbose_name='테이블개수'),
        ),
    ]
