# Generated by Django 3.0.6 on 2020-07-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0268_auto_20200720_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbdetail',
            options={'verbose_name': 'Database(서버 레벨) 추가', 'verbose_name_plural': 'Database(서버 레벨) 추가'},
        ),
        migrations.AlterModelOptions(
            name='dblist',
            options={'ordering': ['db_use'], 'verbose_name': 'Database(서비스 레벨) 추가', 'verbose_name_plural': 'Database(서비스 레벨) 추가'},
        ),
        migrations.AlterModelOptions(
            name='metareqweekday',
            options={'verbose_name': '정기반영 대상 지정', 'verbose_name_plural': '정기반영 대상 지정'},
        ),
        migrations.AlterModelOptions(
            name='monitoritemlist',
            options={'verbose_name': '모니터링 항목', 'verbose_name_plural': '모니터링 항목'},
        ),
        migrations.AlterModelOptions(
            name='monitoritemlog',
            options={'verbose_name': '모니터링 LOG', 'verbose_name_plural': '모니터링 LOG'},
        ),
        migrations.AlterModelOptions(
            name='monitortablespace',
            options={'verbose_name': '테이블스페이스 모니터링, 임계치 조정', 'verbose_name_plural': '테이블스페이스 모니터링, 임계치 조정'},
        ),
        migrations.RemoveField(
            model_name='dbdetail',
            name='active_yn',
        ),
        migrations.RemoveField(
            model_name='dbdetail',
            name='conct_succs_yn',
        ),
        migrations.AlterField(
            model_name='stdattr',
            name='reject_exp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='반려사유'),
        ),
    ]
