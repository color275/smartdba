# Generated by Django 2.1.5 on 2020-03-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0113_remove_batchlist_truncate_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchlist',
            name='truncate_yn',
            field=models.CharField(choices=[('1', 'Y'), ('0', 'N')], default='0', max_length=30, verbose_name='Truncate여부'),
        ),
    ]
