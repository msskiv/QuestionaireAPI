# Generated by Django 3.2.4 on 2021-06-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20210619_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='session',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='ключ сессии'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='пользователь'),
        ),
    ]
