# Generated by Django 3.2.7 on 2021-09-26 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ['date'], 'verbose_name': 'Статистика', 'verbose_name_plural': 'Статистика'},
        ),
    ]
