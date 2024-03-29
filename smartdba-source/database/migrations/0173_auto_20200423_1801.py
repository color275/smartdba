# Generated by Django 2.1.5 on 2020-04-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0172_auto_20200422_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablelist',
            name='secu_yn',
            field=models.CharField(blank=True, choices=[('1', 'Y'), ('0', 'N')], max_length=30, null=True, verbose_name='개인정보여부'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='id_dblist',
            field=models.ForeignKey(blank=True, db_column='id_dblist', default=10, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.DbList', verbose_name='DB명'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='id_domain',
            field=models.ForeignKey(blank=True, db_column='id_domain', default=3, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.Domain', verbose_name='업무도메인명'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='id_tuningstatus',
            field=models.ForeignKey(blank=True, db_column='id_tuningstatus', default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.TuningStatus', verbose_name='튜닝진행상태'),
        ),
    ]
