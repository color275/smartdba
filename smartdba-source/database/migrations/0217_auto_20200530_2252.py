# Generated by Django 2.1.5 on 2020-05-30 22:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0216_auto_20200530_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoritemlist',
            name='lv2_item_nm',
            field=models.CharField(blank=True, help_text='"parameter 명 사용되며 알파벳+언더바만 사용 가능', max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z_]*$', '영문,언더바(_)만 입력 가능합니다.')], verbose_name='하위 모니터링 항목'),
        ),
    ]
