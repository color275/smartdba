# Generated by Django 2.1.5 on 2020-03-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0101_userrequesttabprivhist_id_tablelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequesttabprivhist',
            name='approv_yn',
            field=models.CharField(choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, verbose_name='승인여부'),
        ),
    ]
