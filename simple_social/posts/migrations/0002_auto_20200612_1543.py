# Generated by Django 3.0.6 on 2020-06-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]
