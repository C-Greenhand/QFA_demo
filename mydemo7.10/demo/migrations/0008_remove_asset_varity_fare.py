# Generated by Django 2.2.3 on 2019-07-10 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_bond'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset_varity',
            name='fare',
        ),
    ]