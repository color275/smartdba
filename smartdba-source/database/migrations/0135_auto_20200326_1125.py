# Generated by Django 2.1.5 on 2020-03-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0134_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='expl',
            field=models.TextField(blank=True, null=True, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='word',
            name='std_wd_eng',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='영문단어명'),
        ),
        migrations.AlterField(
            model_name='word',
            name='std_wd_eng_ful',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='영문FULL명'),
        ),
        migrations.AlterField(
            model_name='word',
            name='std_wd_kor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='한글단어명'),
        ),
    ]
