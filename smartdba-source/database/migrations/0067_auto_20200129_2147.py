# Generated by Django 2.1.5 on 2020-01-29 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0066_auto_20200128_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalist',
            name='prov_yn1_dtm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='보안 승인 일자'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datalist',
            name='prov_yn2_dtm',
            field=models.DateTimeField(auto_now=True, verbose_name='성능 승인 일자'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='id_prov_user1',
            field=models.ForeignKey(blank=True, db_column='id_prov_user1', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DataList_prov_user1', to=settings.AUTH_USER_MODEL, verbose_name='2차 승인(보안)'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='id_prov_user2',
            field=models.ForeignKey(blank=True, db_column='id_prov_user2', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DataList_prov_user2', to=settings.AUTH_USER_MODEL, verbose_name='1차 승인(성능)'),
        ),
    ]
