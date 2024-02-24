# Generated by Django 2.1.5 on 2020-03-17 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0111_auto_20200317_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchlist',
            name='truncate_yn',
            field=models.CharField(choices=[('1', 'insert_direct'), ('0', 'truncate_insert')], default='1', max_length=30, verbose_name='Truncate여부'),
        ),
        migrations.AlterField(
            model_name='objectsource',
            name='id_objectlist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', on_delete=django.db.models.deletion.DO_NOTHING, to='database.ObjectList', verbose_name='오브젝트명ID'),
        ),
    ]
