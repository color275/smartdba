# Generated by Django 3.0.6 on 2020-11-24 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0298_auto_20201124_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbdetail',
            name='id_dbposition',
            field=models.ForeignKey(blank=True, db_column='id_dbposition', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.DbPosition', verbose_name='DBMS위치'),
        ),
    ]
