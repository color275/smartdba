# Generated by Django 3.0.6 on 2020-06-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0242_auto_20200608_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdattr',
            name='accept_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, null=True, verbose_name='승인여부'),
        ),
    ]
