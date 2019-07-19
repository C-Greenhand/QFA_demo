# Generated by Django 2.2.3 on 2019-07-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASSET_TYPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=64)),
                ('ratio', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('cap', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='ASSET_VARITY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=64)),
                ('fare', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('asset_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_TYPE')),
            ],
        ),
        migrations.CreateModel(
            name='BRENT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='COMMON_INFORMATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_space', models.IntegerField(default=0)),
                ('sum_cap', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('income', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='FACTORY_TYPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=64)),
                ('exchange_rate', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='FX_RATE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('close', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='INTEREST_RATE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('close', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='PMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('manufacture', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='ZZ_500S',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('close', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='WEIGHT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('asset_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_TYPE')),
                ('factory_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.FACTORY_TYPE')),
            ],
        ),
        migrations.CreateModel(
            name='RB_NH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('close', models.DecimalField(decimal_places=3, max_digits=15)),
                ('asset_varity', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_VARITY')),
            ],
        ),
        migrations.CreateModel(
            name='J_NH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('asset_varity', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_VARITY')),
            ],
        ),
        migrations.CreateModel(
            name='FACTORY_PRICE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('factory_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.FACTORY_TYPE')),
            ],
        ),
        migrations.CreateModel(
            name='CU_NH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('asset_varity', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_VARITY')),
            ],
        ),
        migrations.CreateModel(
            name='ASSET_PRICE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('asset_varity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_VARITY')),
            ],
        ),
        migrations.CreateModel(
            name='AL_NH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('asset_varity', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='demo.ASSET_VARITY')),
            ],
        ),
    ]
