# Generated by Django 3.0.4 on 2020-03-24 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerHouseHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerRefno', models.IntegerField(unique=True, verbose_name='Reference Number')),
                ('customerMetreno', models.BigIntegerField(unique=True, verbose_name='Metre Number')),
                ('customerAccno', models.IntegerField(unique=True, verbose_name='Account Number')),
                ('customerFirstName', models.CharField(max_length=120, verbose_name='First name')),
                ('customerLastName', models.CharField(max_length=120, verbose_name='Last name')),
                ('customerLat', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Customer Latitude')),
                ('customerLong', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Customer Longtitue')),
                ('customerPhone', models.CharField(max_length=11, verbose_name='Customer Phone Number')),
            ],
            options={
                'verbose_name': 'Customer House hold',
                'verbose_name_plural': 'Customer House Holds',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Bought')),
                ('units', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Units')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='customer.CustomerHouseHold')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='MetreReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(verbose_name='Date Bought')),
                ('voltage', models.IntegerField(verbose_name='metre voltage')),
                ('current', models.IntegerField(verbose_name='metre current')),
                ('consumption', models.IntegerField(verbose_name='metre consumption')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metre', to='customer.CustomerHouseHold')),
            ],
            options={
                'verbose_name': 'Metre Reading',
                'verbose_name_plural': 'Metre Readings',
            },
        ),
    ]
