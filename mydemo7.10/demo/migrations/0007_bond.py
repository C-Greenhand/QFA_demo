# Generated by Django 2.2.3 on 2019-07-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20190709_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOND',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('cap', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
    ]
