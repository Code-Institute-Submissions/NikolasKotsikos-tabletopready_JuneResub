# Generated by Django 3.1.7 on 2021-04-22 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0017_auto_20210420_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miniature',
            options={'ordering': ['gamesys']},
        ),
    ]
