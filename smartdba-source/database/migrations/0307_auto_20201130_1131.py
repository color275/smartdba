# Generated by Django 3.0.6 on 2020-11-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0306_auto_20201130_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitoritemlist',
            name='item_nm',
        ),
        migrations.AddField(
            model_name='monitoritem',
            name='sms_message',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='알람 메시지'),
        ),
    ]
