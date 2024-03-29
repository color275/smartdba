# Generated by Django 2.1.5 on 2020-03-26 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0136_auto_20200326_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='도메인명')),
                ('info_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='인포타입')),
                ('data_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='데이터타입')),
                ('leng', models.CharField(blank=True, max_length=100, null=True, verbose_name='데이터길이')),
                ('decimal_leng', models.CharField(blank=True, max_length=100, null=True, verbose_name='데이터길이')),
                ('expl', models.TextField(blank=True, null=True, verbose_name='설명')),
            ],
            options={
                'verbose_name': '[DBA-99] 표준도메인',
                'verbose_name_plural': '[DBA-99] 표준도메인',
                'db_table': 'cust_std_domain',
            },
        ),
        migrations.RenameModel(
            old_name='STD_WORD',
            new_name='StdWord',
        ),
        migrations.RemoveField(
            model_name='std_domain',
            name='id_std_domaintype',
        ),
        migrations.RenameModel(
            old_name='STD_DOMAIN_TYPE',
            new_name='StdDomainType',
        ),
        migrations.DeleteModel(
            name='STD_DOMAIN',
        ),
        migrations.AddField(
            model_name='stddomain',
            name='id_std_domaintype',
            field=models.ForeignKey(blank=True, db_column='id_std_domaintype', null=True, on_delete=django.db.models.deletion.PROTECT, to='database.StdDomainType', verbose_name='도메인타입'),
        ),
    ]
