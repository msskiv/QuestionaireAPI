# Generated by Django 3.2.4 on 2021-06-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_dt', models.DateTimeField(auto_now=True)),
                ('quest_end_dt', models.DateTimeField(verbose_name='Дата окончания опроса')),
                ('quest_name', models.CharField(max_length=200, verbose_name='Название опроса')),
                ('quest_description', models.TextField(max_length=600, verbose_name='Описание опроса')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]
