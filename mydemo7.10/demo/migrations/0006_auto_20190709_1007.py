# Generated by Django 2.2.3 on 2019-07-09 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20190708_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brent',
            old_name='price',
            new_name='close',
        ),
        migrations.RenameField(
            model_name='pmi',
            old_name='manufacture',
            new_name='close',
        ),
    ]
