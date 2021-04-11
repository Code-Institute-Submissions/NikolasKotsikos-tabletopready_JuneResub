# Generated by Django 3.1.7 on 2021-04-08 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0006_auto_20210408_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='miniature',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='miniature',
            name='faction',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]