# Generated by Django 3.2.4 on 2021-06-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623210308.9178295),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.TextField(default=1623210308.9178295),
        ),
    ]
