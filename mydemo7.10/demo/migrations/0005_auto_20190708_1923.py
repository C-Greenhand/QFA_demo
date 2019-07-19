# Generated by Django 2.2.3 on 2019-07-08 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_zz_500s_asset_varity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='al_nh',
            old_name='price',
            new_name='close',
        ),
        migrations.RenameField(
            model_name='cu_nh',
            old_name='price',
            new_name='close',
        ),
        migrations.RenameField(
            model_name='j_nh',
            old_name='price',
            new_name='close',
        ),
        migrations.RemoveField(
            model_name='al_nh',
            name='asset_varity',
        ),
        migrations.RemoveField(
            model_name='cu_nh',
            name='asset_varity',
        ),
        migrations.RemoveField(
            model_name='j_nh',
            name='asset_varity',
        ),
        migrations.RemoveField(
            model_name='rb_nh',
            name='asset_varity',
        ),
        migrations.RemoveField(
            model_name='zz_500s',
            name='asset_varity',
        ),
    ]
