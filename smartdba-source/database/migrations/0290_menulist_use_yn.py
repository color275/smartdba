# Generated by Django 3.0.6 on 2020-10-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0289_auto_20201015_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='use_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='1', max_length=30, null=True, verbose_name='사용여부'),
        ),
    ]
