# Generated by Django 2.1.5 on 2020-01-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0070_auto_20200129_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='data_explain',
            field=models.TextField(null=True, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='prov_yn1',
            field=models.CharField(choices=[('1', '승인'), ('0', '승인대기'), ('2', '반려')], default='0', max_length=100, null=True, verbose_name='보안 승인여부'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='prov_yn2',
            field=models.CharField(choices=[('1', '승인'), ('0', '승인대기'), ('2', '반려')], default='0', max_length=100, null=True, verbose_name='성능 승인여부'),
        ),
    ]
