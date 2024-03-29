# Generated by Django 3.0.6 on 2020-06-03 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0220_monitortablespace_monitortablespacelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitortablespacelog',
            old_name='usage',
            new_name='usage_percent',
        ),
        migrations.AddField(
            model_name='monitortablespace',
            name='id_mod_user',
            field=models.ForeignKey(blank=True, db_column='id_mod_user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
        migrations.AddField(
            model_name='monitortablespace',
            name='mod_dtm',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='수정일자'),
        ),
        migrations.AddField(
            model_name='monitortablespace',
            name='reg_dtm',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록일자'),
        ),
    ]
