# Generated by Django 2.2.3 on 2019-07-08 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20190708_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zz_500s',
            old_name='price',
            new_name='close',
        ),
    ]