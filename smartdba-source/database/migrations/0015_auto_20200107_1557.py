# Generated by Django 2.1.5 on 2020-01-07 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0014_menulist'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='id_mod_user',
            field=models.ForeignKey(blank=True, db_column='id_mod_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_MenuList_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
        migrations.AddField(
            model_name='menulist',
            name='id_reg_user',
            field=models.ForeignKey(blank=True, db_column='id_reg_user', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_MenuList_reg_user', to=settings.AUTH_USER_MODEL, verbose_name='등록자'),
        ),
        migrations.AddField(
            model_name='menulist',
            name='mod_dtm',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일자'),
        ),
    ]
