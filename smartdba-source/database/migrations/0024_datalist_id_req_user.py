# Generated by Django 2.1.5 on 2020-01-16 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0023_tablelistdatahubdhubown'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalist',
            name='id_req_user',
            field=models.ForeignKey(blank=True, db_column='id_req_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_DataList_req_user', to=settings.AUTH_USER_MODEL, verbose_name='요청자'),
        ),
    ]
