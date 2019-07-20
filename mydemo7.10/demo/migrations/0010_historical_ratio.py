# Generated by Django 2.2.2 on 2019-07-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_asset_varity_cap'),
    ]

    operations = [
        migrations.CreateModel(
            name='HISTORICAL_RATIO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_Ratio', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('Futures_Ratio', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('Bond_Ratio', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
    ]