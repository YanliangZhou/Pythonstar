# Generated by Django 3.1.5 on 2021-01-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('time', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('side', models.CharField(default='', max_length=200)),
                ('qty', models.CharField(default='', max_length=200)),
                ('symbol', models.CharField(default='', max_length=200)),
                ('px', models.CharField(default='', max_length=200)),
                ('exchange', models.CharField(default='', max_length=200)),
                ('class_type', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('tags', models.CharField(default='', max_length=200)),
                ('local_time', models.CharField(default='', max_length=200)),
                ('source', models.CharField(default='', max_length=200)),
                ('orderID', models.CharField(default='', max_length=200)),
                ('exchangeOID', models.CharField(default='', max_length=200)),
                ('fillID', models.CharField(default='', max_length=200)),
                ('strategy', models.CharField(default='', max_length=200)),
                ('ilink', models.CharField(default='', max_length=200)),
                ('px_multiplier', models.CharField(default='', max_length=200)),
                ('multiplier', models.CharField(default='', max_length=200)),
                ('TO', models.CharField(default='', max_length=200)),
                ('OC', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
