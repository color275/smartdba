# Generated by Django 3.0.6 on 2020-10-15 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0288_auto_20201015_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoritemlog',
            name='id_dbdetail',
            field=models.ForeignKey(blank=True, db_column='id_dbdetail', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbDetail', verbose_name='DB상세'),
        ),
        migrations.AlterField(
            model_name='monitoritemlog',
            name='id_dblist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbList', verbose_name='DB용도'),
        ),
        migrations.AlterField(
            model_name='monitoritemlog',
            name='id_dbtype',
            field=models.ForeignKey(blank=True, db_column='id_dbtype', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DbType', verbose_name='DBMS종류'),
        ),
        migrations.AlterField(
            model_name='monitoritemlog',
            name='id_opercd',
            field=models.ForeignKey(blank=True, db_column='id_opercd', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.OperCd', verbose_name='운영구분'),
        ),
    ]
