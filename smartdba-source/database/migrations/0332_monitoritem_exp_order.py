# Generated by Django 3.0.6 on 2020-12-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0331_auto_20201207_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoritem',
            name='exp_order',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='화면노출순서'),
        ),
    ]
