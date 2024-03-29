# Generated by Django 2.1.5 on 2020-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0210_auto_20200529_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbdetail',
            options={'verbose_name': 'Database(서버 레벨)', 'verbose_name_plural': 'Database(서버 레벨)'},
        ),
        migrations.AlterModelOptions(
            name='dblist',
            options={'ordering': ['db_use'], 'verbose_name': 'Database(서비스 레벨)', 'verbose_name_plural': 'Database(서비스 레벨)'},
        ),
        migrations.AddField(
            model_name='monitoritemlog',
            name='monitor_title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='제목(key)'),
        ),
        migrations.AlterField(
            model_name='monitoritemlog',
            name='monitor_value',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='값(value)'),
        ),
    ]
