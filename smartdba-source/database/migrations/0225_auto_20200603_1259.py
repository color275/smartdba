# Generated by Django 3.0.6 on 2020-06-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0224_auto_20200603_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitortablespace',
            name='explain',
            field=models.TextField(max_length=100, null=True, verbose_name='비고'),
        ),
    ]
