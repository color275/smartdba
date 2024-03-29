# Generated by Django 2.1.5 on 2020-02-17 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0074_auto_20200216_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarequest',
            name='poss_view_dtm',
            field=models.DateTimeField(null=True, verbose_name='조회가능일자'),
        ),
        migrations.AlterField(
            model_name='datarequest',
            name='data_explain',
            field=models.TextField(blank=True, null=True, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='datarequest',
            name='id_prov_user',
            field=models.ForeignKey(blank=True, db_column='id_prov_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DataRequest_prov_user1', to=settings.AUTH_USER_MODEL, verbose_name='검토자'),
        ),
        migrations.AlterField(
            model_name='datarequest',
            name='prov_yn',
            field=models.CharField(blank=True, choices=[('1', '승인'), ('0', '승인대기'), ('2', '반려')], default='0', max_length=100, null=True, verbose_name='검토여부'),
        ),
        migrations.AlterField(
            model_name='datarequest',
            name='prov_yn_dtm',
            field=models.DateTimeField(null=True, verbose_name='검토일자'),
        ),
    ]
