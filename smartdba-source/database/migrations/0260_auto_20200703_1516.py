# Generated by Django 3.0.6 on 2020-07-03 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0259_stdattr_use_yn'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdDataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_typ_nm', models.CharField(blank=True, max_length=100, null=True, verbose_name='데이터타입명')),
            ],
            options={
                'verbose_name': '데이터타입',
                'verbose_name_plural': '데이터타입',
                'db_table': 'cust_std_data_type',
            },
        ),
        migrations.AddField(
            model_name='stddomain',
            name='id_stddatatype',
            field=models.ForeignKey(blank=True, db_column='id_stddatatype', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.StdDataType', verbose_name='데이터타입명'),
        ),
    ]
