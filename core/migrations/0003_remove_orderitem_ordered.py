# Generated by Django 2.2.14 on 2021-05-10 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210510_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
    ]
