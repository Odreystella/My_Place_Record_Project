# Generated by Django 3.2.4 on 2021-06-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20210609_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1623210358.3918428),
        ),
    ]
