# Generated by Django 2.1.5 on 2020-01-06 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20200106_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexecutesql',
            name='id_datalist',
            field=models.ForeignKey(blank=True, db_column='id_datalist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DataList', verbose_name='데이터리스트'),
        ),
    ]
