# Generated by Django 2.1.5 on 2020-01-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0048_auto_20200126_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuninglist',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]
