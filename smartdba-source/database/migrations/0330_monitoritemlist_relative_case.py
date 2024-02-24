# Generated by Django 3.0.6 on 2020-12-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0329_auto_20201205_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoritemlist',
            name='relative_case',
            field=models.CharField(choices=[('0', '누적값'), ('1', '상대값')], default=0, max_length=30, verbose_name='누적값 여부'),
        ),
    ]
