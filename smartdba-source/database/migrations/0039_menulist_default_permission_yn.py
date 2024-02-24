# Generated by Django 2.1.5 on 2020-01-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0038_menupermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='default_permission_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, null=True, verbose_name='기본권한'),
        ),
    ]
