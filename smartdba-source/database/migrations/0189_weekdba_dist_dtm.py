# Generated by Django 2.1.5 on 2020-05-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0188_auto_20200511_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekdba',
            name='dist_dtm',
            field=models.DateField(blank=True, null=True, verbose_name='정기반영일자'),
        ),
    ]
