# Generated by Django 3.0.6 on 2020-10-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0290_menulist_use_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='URL'),
        ),
    ]
