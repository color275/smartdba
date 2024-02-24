# Generated by Django 3.0.6 on 2020-12-01 18:23

from django.db import migrations
import django_safe_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0315_osuser_passwd2'),
    ]

    operations = [
        migrations.AddField(
            model_name='osuser',
            name='password3',
            field=django_safe_fields.fields.SafeCharField(blank=True, max_length=64, null=True, verbose_name='비밀번호3'),
        ),
        migrations.AlterField(
            model_name='osuser',
            name='password',
            field=django_safe_fields.fields.SafeCharField(blank=True, max_length=64, null=True, verbose_name='비밀번호'),
        ),
    ]
