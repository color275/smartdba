# Generated by Django 3.0.6 on 2020-07-18 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0266_monitoritemlog_elapsed_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoritemlog',
            name='elapsed_time',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='수행시간(초)'),
        ),
    ]
