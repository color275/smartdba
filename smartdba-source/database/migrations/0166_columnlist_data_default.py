# Generated by Django 2.1.5 on 2020-04-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0165_dblist_infra_op_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnlist',
            name='data_default',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='default값'),
        ),
    ]
