# Generated by Django 3.0.6 on 2020-07-20 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0267_auto_20200718_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbowner',
            options={'ordering': ('owner',), 'verbose_name': 'DB Owner명', 'verbose_name_plural': 'DB Owner명'},
        ),
        migrations.AlterModelOptions(
            name='dbtablespace',
            options={'verbose_name': 'OWNER-TABLESPACE 매핑', 'verbose_name_plural': 'OWNER-TABLESPACE 매핑'},
        ),
        migrations.AlterModelOptions(
            name='metagrantdetail',
            options={'verbose_name': 'API(서비스)-권한 매핑', 'verbose_name_plural': 'API(서비스)-권한 매핑'},
        ),
        migrations.AlterModelOptions(
            name='metagrantlist',
            options={'ordering': ('app_service',), 'verbose_name': 'DB-API(서비스) 매핑', 'verbose_name_plural': 'DB-API(서비스) 매핑'},
        ),
        migrations.AddField(
            model_name='userrequesttabprivhist',
            name='use_yn',
            field=models.CharField(choices=[('1', 'Y'), ('0', 'N')], default='1', max_length=30, verbose_name='사용여부'),
        ),
        migrations.AlterField(
            model_name='metagrantdetail',
            name='id_metagrantlist',
            field=models.ForeignKey(blank=True, db_column='id_metagrantlist', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.MetaGrantList', verbose_name='API(서비스)'),
        ),
        migrations.AlterField(
            model_name='metagrantlist',
            name='app_service',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='API(서비스)'),
        ),
    ]
