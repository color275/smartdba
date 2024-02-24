# Generated by Django 2.1.5 on 2020-03-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0132_auto_20200324_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='', max_length=100, verbose_name='DB명')),
            ],
            options={
                'verbose_name': '[DBA-99] DB Owner명',
                'verbose_name_plural': '[DBA-99] DB Owner명',
                'db_table': 'cust_owner',
            },
        ),
        migrations.AlterField(
            model_name='grantlist',
            name='table_name',
            field=models.CharField(max_length=100, null=True, verbose_name='table_name'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='sql_id',
            field=models.CharField(max_length=1000, null=True, verbose_name='SQL_ID'),
        ),
        migrations.AlterField(
            model_name='tuninglist',
            name='title',
            field=models.CharField(max_length=1000, null=True, verbose_name='제목'),
        ),
    ]
