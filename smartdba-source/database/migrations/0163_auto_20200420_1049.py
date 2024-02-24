# Generated by Django 2.1.5 on 2020-04-20 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0162_auto_20200419_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='metareq',
            name='id_req_prod',
            field=models.ForeignKey(blank=True, db_column='id_req_prod', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='metareq_id_req_prod', to=settings.AUTH_USER_MODEL, verbose_name='운영반영요청자'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='req_prod_comment',
            field=models.CharField(max_length=200, null=True, verbose_name='운영반영요청의견'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='req_prod_dtm',
            field=models.DateTimeField(blank=True, null=True, verbose_name='운영반영요청시간'),
        ),
        migrations.AddField(
            model_name='metareq',
            name='req_prod_yn',
            field=models.CharField(blank=True, choices=[('0', '승인 전'), ('1', '승인'), ('2', '반려')], default=0, max_length=200, null=True, verbose_name='운영반영요청여부'),
        ),
    ]
