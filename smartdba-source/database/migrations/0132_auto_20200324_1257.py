# Generated by Django 2.1.5 on 2020-03-24 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0131_remove_grantlist_id_reg_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantlist',
            name='id_tablelist',
            field=models.ForeignKey(blank=True, db_column='id_tablelist', max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.TableList', verbose_name='테이블명'),
        ),
        migrations.AddField(
            model_name='grantlist',
            name='id_userlist',
            field=models.ForeignKey(blank=True, db_column='id_userlist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.UserList', verbose_name='User명'),
        ),
    ]
