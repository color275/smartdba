# Generated by Django 3.0.6 on 2020-06-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0221_auto_20200603_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitortablespacelog',
            name='total',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='전체사이즈'),
        ),
    ]
